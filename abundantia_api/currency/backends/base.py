import requests

from django.conf import settings

from ..models import Currency

CURRENCY_CLIENTS_TIMEOUT = getattr(settings, "CURRENCY_CLIENTS_TIMEOUT", (5.0, 30.0))


class BaseClient:
    TIMEOUT = CURRENCY_CLIENTS_TIMEOUT

    def __init__(self):
        self.base_url = ""
        self.token = ""

    def get_connection_exceptions(self):
        return requests.TooManyRedirects, requests.ConnectionError, requests.Timeout

    def build_url(self, endpoint):
        url = self.base_url.format(f"{endpoint}?key={self.token}")
        return url

    def get(self, url):
        # May raise: requests.TooManyRedirects, requests.ConnectionError, requests.Timeout
        return requests.get(url)


class BaseBackend:

    id = "base"

    def _get_currencies(self):
        currency_queryset = Currency.objects.active()

        return currency_queryset

    def update(self):
        raise NotImplementedError("Update not implemented.")
