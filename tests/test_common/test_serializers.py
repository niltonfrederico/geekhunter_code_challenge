import pytest

from autofixture import AutoFixture

from hamcrest import assert_that, has_key

from abundantia_api.currency.models import Currency
from ..fixtures.fake_serializers import FakeReadSerializer, FakeWriteSerializer


pytestmark = pytest.mark.django_db


def test_base_read_serializer():
    currency = AutoFixture(Currency).create_one()

    serializer = FakeReadSerializer(instance=currency)

    assert_that(serializer.data, has_key("id"))
    assert_that(serializer.data, has_key("created"))
    assert_that(serializer.data, has_key("modified"))


def test_base_write_serializer():
    data = {"code": "FAK", "name": "Fake currency"}

    serializer = FakeWriteSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    instance = serializer.save()

    assert_that(serializer.data, has_key("id"))
    assert_that(serializer.data, has_key("created"))
    assert_that(serializer.data, has_key("modified"))
