import pytest

from autofixture import AutoFixture

from abundantia_api.currency.models import Currency, Quotation


pytestmark = pytest.mark.django_db


def test_currency_create():
    # Basic Django Model test
    assert Currency.objects.all().count() == 0

    currency = AutoFixture(Currency, generate_fk=True).create_one()

    assert currency
    assert Currency.objects.all().count() == 1


def test_quotations_create():
    # Basic Django Model test
    assert Quotation.objects.all().count() == 0

    quotation = AutoFixture(Quotation, generate_fk=True).create_one()

    assert quotation
    assert Quotation.objects.all().count() == 1
