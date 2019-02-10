from django.db.models import Manager
from django.db.models.query import QuerySet


class BaseQuerySet(QuerySet):
    def active(self):
        return self.filter(is_active=True)


class BaseManager(Manager):
    def get_queryset(self):
        return BaseQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()
