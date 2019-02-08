from django.conf import settings

from ..models import Currency

CURRENCY_CLIENTS_TIMEOUT = getattr(settings, "CURRENCY_CLIENTS_TIMEOUT", (5.0, 30.0))


class BaseClient:
    TIMEOUT = CURRENCY_CLIENTS_TIMEOUT


class BaseBackend:
    def _get_currencies(self):
        currency_queryset = Currency.objects.active()

        return currency_queryset

    def update(self):
        raise NotImplementedError("Update not implemented.")
