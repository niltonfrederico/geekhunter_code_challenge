from decimal import Decimal

import pytest
import vcr

from autofixture import AutoFixture
from hamcrest import assert_that, has_entries

from abundantia_api.currency.models import Currency, Quotation
from abundantia_api.currency.backends.base import BaseClient
from abundantia_api.currency.backends import QuotationsBackendManager
from abundantia_api.currency.backends.hgbrasil.clients import HGBrasilClient


pytestmark = pytest.mark.django_db

client_vcr = vcr.VCR(
    cassette_library_dir="tests/test_currency/test_backends/fixtures/cassettes",
    record_mode="once",
    match_on=["uri", "method"],
)


def test_get_backends():
    pass


def test_backend_get_currencies():
    pass


@client_vcr.use_cassette()
def test_backend_update_simple():
    currency = AutoFixture(Currency, {"code": "USD", "name": "Dollar"}).create_one()

    backend_class = QuotationsBackendManager.get_backend("hgbrasil")
    backend = backend_class()

    backend.update()

    quotations_queryset = Quotation.objects.all()

    assert quotations_queryset.count() == 1

    quotation = quotations_queryset.first()

    assert quotation.currency_id == currency.id
    assert quotation.amount == Decimal("3.7357")
    assert quotation.variation == Decimal("0.0460")


def test_backend_update_with_no_currency():
    backend_class = QuotationsBackendManager.get_backend("hgbrasil")
    backend = backend_class()

    backend.update()

    quotations_queryset = Quotation.objects.all()

    assert quotations_queryset.count() == 0


def test_backend_update_inactivated_items():
    active_currency = AutoFixture(
        Currency, {"code": "USD", "name": "Dollar"}
    ).create_one()
    AutoFixture(
        Currency,
        {
            "code": "BTC",
            "name": "Bitcoin",
            "is_active": False,
            "is_cryptocurrency": True,
        },
    ).create_one()

    backend_class = QuotationsBackendManager.get_backend("hgbrasil")
    backend = backend_class()

    backend.update()

    quotations_queryset = Quotation.objects.all()

    assert quotations_queryset.count() == 1  # Must return only one result

    quotation = quotations_queryset.first()

    assert quotation.currency_id == active_currency.id
    assert quotation.amount == Decimal("3.7357")
    assert quotation.variation == Decimal("0.0460")
