import pytest

from autofixture import AutoFixture

from hamcrest import assert_that, has_key

from abundantia_api.currency.models import Currency
from ..fixtures.fake_serializer import FakeReadSerializer


pytestmark = pytest.mark.django_db


def test_base_read_serializer():
    currency = AutoFixture(Currency).create_one()

    serializer = FakeReadSerializer(instance=currency)

    assert_that(serializer.data, has_key("id"))
    assert_that(serializer.data, has_key("created"))
    assert_that(serializer.data, has_key("modified"))
