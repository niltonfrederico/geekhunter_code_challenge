import pytest

from rest_framework.exceptions import ErrorDetail

from autofixture import AutoFixture
from rest_framework.reverse import reverse
from hamcrest import assert_that, has_entries

from abundantia_api.currency.models import Currency, Quotation


pytestmark = pytest.mark.django_db


def test_currency_create(api_client):
    data = {"code": "TST", "name": "Currency", "is_active": True}

    url = reverse("currencies:currencies-list")

    response = api_client.post(url, data=data)

    assert response.status_code == 201

    assert_that(
        response.data,
        has_entries(
            {
                "code": "TST",
                "name": "Currency",
                "is_active": True,
                "is_cryptocurrency": False,
            }
        ),
    )


def test_currency_create_duplicate(api_client):
    data = {"code": "TST", "name": "Currency", "is_active": True}

    url = reverse("currencies:currencies-list")

    response = api_client.post(url, data=data)

    assert response.status_code == 201

    response = api_client.post(url, data=data)

    data = response.data
    detail = response.data.get("code")[0]

    assert detail
    assert isinstance(detail, ErrorDetail)
    assert str(detail) == "currency with this code already exists."


def test_currency_list(api_client):
    AutoFixture(Currency).create(5)

    url = reverse("currencies:currencies-list")

    response = api_client.get(url)
    assert response.status_code == 200

    data = response.data
    assert data.get("count") == 5


def test_currency_get(api_client):
    currency = AutoFixture(Currency).create_one()

    url = reverse("currencies:currencies-detail", kwargs={"code": currency.code})

    response = api_client.get(url)

    assert response.status_code == 200

    assert_that(
        response.data,
        has_entries(
            {
                "code": currency.code,
                "name": currency.name,
                "is_active": currency.is_active,
                "is_cryptocurrency": False,
            }
        ),
    )


def test_currency_update(api_client):
    currency = AutoFixture(Currency, {"code": "TST"}).create_one()

    url = reverse("currencies:currencies-detail", kwargs={"code": currency.code})

    response = api_client.put(
        url, data={"name": "updated", "code": currency.code, "is_active": False}
    )

    assert response.status_code == 200

    assert_that(
        response.data,
        has_entries(
            {
                "id": currency.id,
                "code": "TST",
                "name": "updated",
                "is_active": False,
                "is_cryptocurrency": False,
            }
        ),
    )


def test_read_currency_with_quotations_serializer(api_client):
    quotation = AutoFixture(
        Quotation,
        field_values={"amount": 10.5001, "variation": 0.0001},
        generate_fk=True,
    ).create_one()
    currency = quotation.currency

    url = reverse("currencies:currencies-quotations", kwargs={"code": currency.code})

    response = api_client.get(url)

    assert response.status_code == 200

    data = response.data

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
