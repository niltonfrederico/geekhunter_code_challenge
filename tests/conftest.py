import pytest


@pytest.fixture
def serializer_context(rf):
    return {"request": rf.get("/")}
