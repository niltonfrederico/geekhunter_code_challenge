from django.db import models

from abundantia_api.common.models import BaseModel
from abundantia_api.currency.backends import QuotationsBackendManager


class Currency(BaseModel):

    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=16)
    is_active = models.BooleanField(default=True)
    is_cryptocurrency = models.BooleanField(default=False)

    def __str__(self):
        return f"({self.id}) {self.code}"


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
