from django.db import models

from model_utils.models import TimeStampedModel

from .managers import BaseManager


class BaseModel(TimeStampedModel):

    objects = BaseManager()

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)
