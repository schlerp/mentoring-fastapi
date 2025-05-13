# Mentoring - FastAPI

This is a project for exploring mentoring via pair programming using FastAPI as the base.

# Steps

## Step 1

<details>
    <summary>Set up the project using UV and setup a basic tests folder.</summary>
    <br>
    The following are the commands I used:

```bash
# from the folder you house your repos in
uv init --lib ./mentoring-fastapi

# add the fastapi dependency
uv add "fastapi[standard]"
```

`main.py` should look like the following at this point:

```python
from fastapi import FastAPI
import pydantic

app = FastAPI()


class EchoResponse(pydantic.BaseModel):
    greeting: str


@app.get("/echo/{name}")
async def echo(name: str) -> EchoResponse:
    return EchoResponse(greeting=f"Hello {name}!")
```

```bash
# add pytest as a dev dependency
uv add --dev pytest
```

Add the following to `src/tests/api/conftest.py` (don't forget to create the `__init__.py` files!)

```python
import pytest
from fastapi import testclient

from mentoring_fastapi import main


@pytest.fixture(name="client")
def _get_client() -> testclient.TestClient:  # pyright: ignore [reportUnusedFunction]
    client = testclient.TestClient(main.app)
    return client
```

Add the following to `src/tests/api/test_main.py`

```python
import pytest
from fastapi import testclient


class TestEchoGet:
    @pytest.mark.parametrize("name", ["test", "test2", "john"])
    def test_echo_get(self, name: str, client: testclient.TestClient) -> None:
        response = client.get(f"/echo/{name}")

        assert response.status_code == 200
        assert response.json() == {"greeting": f"Hello {name}!"}
```

</details>
