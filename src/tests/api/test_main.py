import pytest
from fastapi import testclient


class TestEchoGet:
    @pytest.mark.parametrize("name", ["test", "test2", "john"])
    def test_echo_get(self, name: str, client: testclient.TestClient) -> None:
        response = client.get(f"/echo/{name}")

        assert response.status_code == 200
        assert response.json() == {"greeting": f"Hello {name}!"}
