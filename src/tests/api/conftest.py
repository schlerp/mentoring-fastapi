import pytest
from fastapi import testclient

from mentoring_fastapi import main


@pytest.fixture(name="client")
def _get_client() -> testclient.TestClient:  # pyright: ignore [reportUnusedFunction]
    client = testclient.TestClient(main.app)
    return client
