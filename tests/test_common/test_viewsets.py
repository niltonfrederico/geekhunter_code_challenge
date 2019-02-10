import pytest

from unittest import mock

from autofixture import AutoFixture

from hamcrest import assert_that, has_key

from abundantia_api.currency.models import Currency
from ..fixtures.fake_serializers import FakeReadSerializer, FakeWriteSerializer
from ..fixtures.fake_viewsets import FakeViewSet

pytestmark = pytest.mark.django_db


def test_get_serializer_class():
    viewset = FakeViewSet()

    with mock.patch.object(viewset, "action", return_value="default"):
        assert viewset.get_serializer_class() is FakeReadSerializer

    with mock.patch.object(viewset, "action", return_value="default"):
        assert viewset.get_serializer_class() is FakeWriteSerializer

    assert viewset.get_serializer_class() is FakeReadSerializer
