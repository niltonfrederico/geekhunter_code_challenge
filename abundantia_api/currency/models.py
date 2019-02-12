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

    def _sum_quotations_variation(self, quotation_queryset):
        # This is being done this way to increase perfomance.
        variations = [Decimal(quotation.variation) for quotation in quotation_queryset]
        total = sum(variations)

        return total

    def get_last_day_quotation(self):
        quotation_queryset = self.quotations.filter(
            created__gte=timezone.localdate(), created__lte=timezone.localdate()
        )

        return self._sum_quotations_variation(quotation_queryset)

    def get_last_week_quotation(self):
        start_date = timezone.localdate() - relativedelta(days=7)

        quotation_queryset = self.quotations.filter(
            created__gte=start_date, created__lte=timezone.localdate()
        )

        return self._sum_quotations_variation(quotation_queryset)

    def get_last_month_quotation(self):
        start_date = timezone.localdate().replace(day=1)

        quotation_queryset = self.quotations.filter(
            created__gte=start_date, created__lte=timezone.localdate()
        )

        return self._sum_quotations_variation(quotation_queryset)


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
