import pytest
import vcr

from unittest import mock

from autofixture import AutoFixture

from hamcrest import assert_that, has_entries

from abundantia_api.currency.models import Currency, Quotation
from abundantia_api.currency.backends.base import BaseClient
from abundantia_api.currency.backends import QuotationsBackendManager
from abundantia_api.currency.backends.hgbrasil.clients import HGBrasilClient


pytestmark = pytest.mark.django_db


def test_get_backends():
    pass


def test_backend_get_currencies():
    pass


def test_backend_update_simple():
    AutoFixture(Currency, {"code": "USD", "name": "Dollar"}).create_one()

    backend_class = QuotationsBackendManager.get_backend("hgbrasil")
    backend = backend_class()

    backend.update()


def test_backend_update_with_bitcoin():
    pass


def test_backend_update_with_no_currency():
    pass


def test_backend_update_inactivated_items():
    pass
