from decimal import Decimal

from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta

from abundantia_api.common.models import BaseModel
from abundantia_api.currency.backends import QuotationsBackendManager


class Currency(BaseModel):

    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=16)
    is_active = models.BooleanField(default=True)
    is_cryptocurrency = models.BooleanField(default=False)

    def __str__(self):
        return f"({self.id}) {self.code}"

    def _calculate_quotations_variation(self, quotation_queryset):
        total_quotations = quotation_queryset.count()

        if total_quotations <= 0:
            return 0

        # This is being done this way to increase perfomance.
        variations = [Decimal(quotation.variation) for quotation in quotation_queryset]
        total_sum = sum(variations)

        total = total_sum / total_quotations

        return total.quantize(Decimal(".0001"))

    def get_last_day_quotation(self):
        now = timezone.now()
        start_day = now.replace(hour=0, minute=0, second=0)
        end_day = now.replace(hour=23, minute=59, second=59)

        quotation_queryset = self.quotations.filter(created__gte=start_day).filter(
            created__lte=end_day
        )

        return self._calculate_quotations_variation(quotation_queryset)

    def get_last_week_quotation(self):
        start_date = timezone.now() - relativedelta(days=7)

        quotation_queryset = self.quotations.filter(created__gte=start_date).filter(
            created__lte=timezone.now()
        )

        return self._calculate_quotations_variation(quotation_queryset)

    def get_last_month_quotation(self):
        start_date = timezone.now().replace(day=1)

        quotation_queryset = self.quotations.filter(created__gte=start_date).filter(
            created__lte=timezone.now()
        )

        return self._calculate_quotations_variation(quotation_queryset)


class Quotation(BaseModel):

    backend_id = models.CharField(
        max_length=32,
        choices=QuotationsBackendManager.get_backends_ids(),
        db_index=True,
    )
    currency = models.ForeignKey(
        Currency, related_name="quotations", on_delete=models.CASCADE
    )
    amount = models.DecimalField(max_digits=12, decimal_places=4)
    variation = models.DecimalField(max_digits=12, decimal_places=4)
