import pytest

from autofixture import AutoFixture

from hamcrest import assert_that, has_entries

from abundantia_api.currency.models import Currency
from abundantia_api.currency.serializers import CurrencyReadSerializer


pytestmark = pytest.mark.django_db


def test_read_serializer():
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
