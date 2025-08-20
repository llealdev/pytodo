import pytest
from fastapi.testclient import TestClient

from brax.app import app


@pytest.fixture
def client():
    return TestClient(app)
