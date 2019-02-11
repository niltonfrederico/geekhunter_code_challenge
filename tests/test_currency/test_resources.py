import pytest

from autofixture import AutoFixture
from rest_framework.reverse import reverse
from hamcrest import assert_that, has_entries

from abundantia_api.currency.models import Currency, Quotation


pytestmark = pytest.mark.django_db


def test_currency_create(api_client):
    import ipdb

    ipdb.set_trace()
    url = reverse("currencies:currencies-list")

    response = api_client.get(url)

