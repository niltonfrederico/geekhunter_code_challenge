from django.db.models import Manager
from django.db.models.query import QuerySet


class BaseQuerySet(QuerySet):
    def active(self):
        return self.filter(is_active=True)


class BaseManager(Manager):
    def active(self):
        return self.get_queryset().active()
