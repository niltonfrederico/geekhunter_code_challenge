from django.db import models

from model_utils.choices import Choices

from abundantia_api.common.models import BaseModel


class Currency(BaseModel):

    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=16)
    is_active = models.BooleanField(default=True)


class Quotation(BaseModel):

    currency = models.ForeignKey(
        Currency, related_name="quotations", on_delete=models.CASCADE
    )
    amount = models.DecimalField(max_digits=12, decimal_places=4)
    variation = models.DecimalField(max_digits=12, decimal_places=4)
