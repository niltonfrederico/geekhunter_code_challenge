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
        has_entries({"code": "TST", "name": "Currency", "is_active": True}),
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

    url = reverse("currencies:currencies-detail", kwargs={"pk": currency.id})

    response = api_client.get(url)

    assert response.status_code == 200

    assert_that(
        response.data,
        has_entries(
            {
                "code": currency.code,
                "name": currency.name,
                "is_active": currency.is_active,
            }
        ),
    )


def test_currency_update(api_client):
    currency = AutoFixture(Currency, {"code": "TST"}).create_one()

    url = reverse("currencies:currencies-detail", kwargs={"pk": currency.id})

    response = api_client.put(
        url, data={"name": "updated", "code": currency.code, "is_active": False}
    )

    assert response.status_code == 200

    assert_that(
        response.data,
        has_entries(
            {"id": currency.id, "code": "TST", "name": "updated", "is_active": False}
        ),
    )
