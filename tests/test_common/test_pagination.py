import pytest
from autofixture import AutoFixture

from rest_framework.reverse import reverse

from abundantia_api.currency.models import Currency


pytestmark = pytest.mark.django_db


def test_previous_and_next_urls(api_client):
    AutoFixture(Currency).create(4)

    url = reverse("currencies:currencies-list")

    response = api_client.get(url, {"limit": 1})

    assert response.status_code == 200
    assert response.data.get("count") == 4

    assert response.data.get("next") == f"{url}?limit=1&offset=1"
    assert response.data.get("previous") is None

    response = api_client.get(url, {"limit": 1, "offset": 1})

    assert response.status_code == 200
    assert response.data.get("count") == 4

    assert response.data["next"] == f"{url}?limit=1&offset=2"
    assert response.data["previous"] == f"{url}?limit=1"

