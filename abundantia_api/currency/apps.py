from django.apps import AppConfig

from .backends import load_backends


class CurrencyConfig(AppConfig):
    name = "abundantia_api.currency"

    def ready(self):
        load_backends()
