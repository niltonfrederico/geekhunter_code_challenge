import pytest

from .helpers import get_api_client


@pytest.fixture(name="context")
def fixture_serializer_context(rf):
    return {"request": rf.get("/")}


@pytest.fixture(name="api_client")
def fixture_api_client():
    return get_api_client()
