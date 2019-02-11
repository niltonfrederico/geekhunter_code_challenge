import pytest

from autofixture import AutoFixture

from hamcrest import assert_that, has_entries

from abundantia_api.currency.models import Currency, Quotation
from abundantia_api.currency.serializers import (
    CurrencyReadSerializer,
    QuotationReadSerializer,
    CurrencyWithQuotationSerializer,
)


pytestmark = pytest.mark.django_db


def test_read_currency_serializer():
    currency = AutoFixture(Currency).create_one()

    serializer = CurrencyReadSerializer(instance=currency)

    assert_that(
        serializer.data,
        has_entries(
            {
                "id": currency.id,
                "name": currency.name,
                "code": currency.code,
                "is_active": currency.is_active,
            }
        ),
    )


def test_read_quotation_serializer():
    quotation = AutoFixture(Quotation, generate_fk=True).create_one()

    serializer = QuotationReadSerializer(instance=quotation)

    assert_that(
        serializer.data,
        has_entries(
            {
                "id": quotation.id,
                "name": quotation.currency.name,
                "code": quotation.currency.code,
                "amount": str(quotation.amount),
                "variation": str(quotation.variation),
            }
        ),
    )


def test_read_currency_with_quotations_serializer():
    quotation = AutoFixture(
        Quotation,
        field_values={"amount": 10.5001, "variation": 0.0001},
        generate_fk=True,
    ).create_one()
    currency = quotation.currency

    serializer = CurrencyWithQuotationSerializer(instance=currency)

    data = serializer.data

    assert_that(
        data,
        has_entries(
            {
                "id": currency.id,
                "name": currency.name,
                "code": currency.code,
                "is_active": currency.is_active,
            }
        ),
    )

    first_quotation = data.get("quotations")[0]

    assert_that(
        first_quotation,
        has_entries(
            {
                "id": quotation.id,
                "name": quotation.currency.name,
                "code": quotation.currency.code,
                "amount": str(quotation.amount),
                "variation": str(quotation.variation),
            }
        ),
    )
