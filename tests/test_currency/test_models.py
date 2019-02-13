from decimal import Decimal
from random import randint

import pytest

from dateutil.relativedelta import relativedelta
from django.utils import timezone

from autofixture import AutoFixture
from autofixture import generators

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


def test_calculate_quotations_variation_without_quotations():
    currency = AutoFixture(Currency).create_one()

    result = currency._calculate_quotations_variation(currency.quotations.all())

    assert result == 0


def test_get_last_day_quotation():
    currency = AutoFixture(Currency).create_one()

    now = timezone.now()
    start_day = now.replace(hour=0, minute=0, second=0)
    end_day = now.replace(hour=23, minute=59, second=59)

    quotations = AutoFixture(
        Quotation,
        {
            "created": generators.DateTimeGenerator(
                min_date=start_day, max_date=end_day
            ),
            "currency": currency,
        },
    ).create(5)

    model_variation = currency.get_last_day_quotation()

    quotations_queryset = Quotation.objects.filter(
        id__in=[quotation.id for quotation in quotations]
    ).order_by("-created")

    first_quotation_amount = Decimal(quotations_queryset.first().amount)
    last_quotation_amount = Decimal(quotations_queryset.last().amount)

    fixture_variation = ((last_quotation_amount * 100) / first_quotation_amount) - 100
    fixture_variation = fixture_variation.quantize(Decimal(".0001"))

    assert model_variation == fixture_variation


def test_get_last_week_quotation():
    currency = AutoFixture(Currency).create_one()

    now = timezone.now()
    start_date = now - relativedelta(days=5)
    end_date = now

    quotations = AutoFixture(
        Quotation,
        {
            "created": generators.DateTimeGenerator(
                min_date=start_date, max_date=end_date
            ),
            "currency": currency,
        },
    ).create(5)

    model_variation = currency.get_last_week_quotation()

    quotations_queryset = Quotation.objects.filter(
        id__in=[quotation.id for quotation in quotations]
    ).order_by("-created")

    first_quotation_amount = Decimal(quotations_queryset.first().amount)
    last_quotation_amount = Decimal(quotations_queryset.last().amount)

    fixture_variation = ((last_quotation_amount * 100) / first_quotation_amount) - 100
    fixture_variation = fixture_variation.quantize(Decimal(".0001"))

    assert model_variation == fixture_variation


def test_get_last_month_quotation():
    currency = AutoFixture(Currency).create_one()

    now = timezone.now()
    start_date = now.replace(day=1)
    end_date = now

    quotations = AutoFixture(
        Quotation,
        {
            "created": generators.DateTimeGenerator(
                min_date=start_date, max_date=end_date
            ),
            "currency": currency,
        },
    ).create(5)

    model_variation = currency.get_last_month_quotation()

    quotations_queryset = Quotation.objects.filter(
        id__in=[quotation.id for quotation in quotations]
    ).order_by("-created")

    first_quotation_amount = Decimal(quotations_queryset.first().amount)
    last_quotation_amount = Decimal(quotations_queryset.last().amount)

    fixture_variation = ((last_quotation_amount * 100) / first_quotation_amount) - 100
    fixture_variation = fixture_variation.quantize(Decimal(".0001"))

    assert model_variation == fixture_variation
