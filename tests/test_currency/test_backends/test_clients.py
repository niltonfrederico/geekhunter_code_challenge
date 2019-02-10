import pytest
import vcr

from unittest import mock

from hamcrest import assert_that, has_entries

from abundantia_api.currency.backends.base import BaseClient
from abundantia_api.currency.backends.hgbrasil.clients import HGBrasilClient


pytestmark = pytest.mark.django_db


FAKE_API_URL = "https://reqres.in/api/{}"


client_vcr = vcr.VCR(
    cassette_library_dir="tests/test_currency/test_backends/fixtures/cassettes",
    record_mode="once",
    match_on=["uri", "method"],
)


@pytest.fixture(name="base_client")
def fixture_base_client():
    base_client = BaseClient()
    base_client.base_url = FAKE_API_URL
    base_client.token = "123456"

    return base_client


@pytest.fixture(name="hgbrasil_client")
def fixture_hgbrasil_client():
    client = HGBrasilClient()

    return client


def test_base_client_build_url(base_client):
    built_url = base_client.build_url("endpoint")

    assert built_url == FAKE_API_URL[:-2] + "endpoint?key=123456"


@client_vcr.use_cassette()
def test_base_client_get(base_client):
    url = base_client.build_url("users")
    response = base_client.get(url)

    assert response.status_code == 200

    response_json = response.json()
    first_result = response_json.get("data")[0]

    assert_that(first_result, has_entries({"id": 1, "first_name": "George"}))


@client_vcr.use_cassette()
def test_hgbrasil_client_get_quotations(hgbrasil_client):
    response = hgbrasil_client.get_quotations()

    assert response.status_code == 200

    response_json = response.json()

    assert_that(
        response_json,
        has_entries(
            {
                "by": "default",
                "valid_key": False,
                "results": {
                    "currencies": {
                        "source": "BRL",
                        "USD": {
                            "name": "Dollar",
                            "buy": 3.734,
                            "sell": None,
                            "variation": 0.625,
                        },
                        "EUR": {
                            "name": "Euro",
                            "buy": 4.2191,
                            "sell": None,
                            "variation": -0.031,
                        },
                        "GBP": {
                            "name": "Pound Sterling",
                            "buy": 4.8293,
                            "sell": None,
                            "variation": 0.07,
                        },
                        "ARS": {
                            "name": "Argentine Peso",
                            "buy": 0.0987,
                            "sell": None,
                            "variation": 0.0,
                        },
                        "BTC": {
                            "name": "Bitcoin",
                            "buy": 14506.85,
                            "sell": 14506.85,
                            "variation": -0.099,
                        },
                    },
                    "stocks": {
                        "IBOVESPA": {
                            "name": "BM&F BOVESPA",
                            "location": "Sao Paulo, Brazil",
                            "points": 95343.102,
                            "variation": 0.99,
                        },
                        "NASDAQ": {
                            "name": "NASDAQ Stock Market",
                            "location": "New York City, United States",
                            "points": 7298.2,
                            "variation": 0.14,
                        },
                        "CAC": {
                            "name": "CAC 40",
                            "location": "Paris, French",
                            "variation": -0.48,
                        },
                        "NIKKEI": {
                            "name": "Nikkei 225",
                            "location": "Tokyo, Japan",
                            "variation": -2.01,
                        },
                    },
                    "available_sources": ["BRL"],
                    "taxes": [],
                },
                "execution_time": 0.0,
                "from_cache": True,
            }
        ),
    )
