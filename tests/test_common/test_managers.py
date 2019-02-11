import pytest

from autofixture import AutoFixture

from abundantia_api.currency.models import Currency


pytestmark = pytest.mark.django_db


def test_queryset_is_active():
    AutoFixture(Currency).create(5)
    AutoFixture(Currency, {"is_active": False}).create(3)

    assert Currency.objects.all().count() == 8
    assert Currency.objects.active().count() == 5
