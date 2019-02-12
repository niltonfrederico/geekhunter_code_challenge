import pytest

from dateutil.relativedelta import relativedelta
from django.utils import timezone

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


def test_get_last_day_quotation():
    currency = AutoFixture(Currency).create_one()

    quotations = AutoFixture(
        Quotation, {"created": timezone.localdate(), "currency": currency}
    ).create(5)

    total = currency.get_last_day_quotation()

    fixture_total = sum([quotation.variation for quotation in quotations])

    assert total == fixture_total


def test_get_last_week_quotation():
    currency = AutoFixture(Currency).create_one()

    start_date = timezone.localdate() - relativedelta(days=5)

    quotations = AutoFixture(
        Quotation, {"created": start_date, "currency": currency}
    ).create(5)

    total = currency.get_last_week_quotation()

    fixture_total = sum([quotation.variation for quotation in quotations])

    assert total == fixture_total


def test_get_last_month_quotation():
    currency = AutoFixture(Currency).create_one()

    start_date = timezone.localdate().replace(day=1)

    quotations = AutoFixture(
        Quotation, {"created": timezone.localdate(), "currency": currency}
    ).create(5)

    total = currency.get_last_month_quotation()

    fixture_total = sum([quotation.variation for quotation in quotations])

    assert total == fixture_total
