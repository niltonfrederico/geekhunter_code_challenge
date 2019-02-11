import importlib

from collections import OrderedDict

from django.conf import settings

LOADED_BACKENDS = OrderedDict()

CURRENCY_QUOTATIONS_BACKENDS = getattr(settings, "CURRENCY_QUOTATIONS_BACKENDS", [])


class QuotationsBackendManager(object):
    @classmethod
    def get_backend(cls, id):
        return LOADED_BACKENDS.get(id, None)

    @classmethod
    def get_backends_ids(cls):
        return [b.id for b in LOADED_BACKENDS.values()]

    @classmethod
    def get_backends(cls):
        return LOADED_BACKENDS.values()


def load_backends():
    for item_str in CURRENCY_QUOTATIONS_BACKENDS:
        module, klass = item_str.rsplit(".", 1)
        module = importlib.import_module(module)

        klass = getattr(module, klass)
        LOADED_BACKENDS[klass.id] = klass
