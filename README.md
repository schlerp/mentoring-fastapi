# Mentoring - FastAPI

This is a project for exploring mentoring via pair programming using FastAPI as the base.

# Steps

## Step 1

<details>
    <summary>Set up the project using UV and setup a basic tests folder.</summary>
    <br>
    The following are the commands I used:

````
```bash
# from the folder you house your repos in
uv init --lib ./mentoring-fastapi

# add the fastapi dependency
uv add "fastapi[standard]"

# write main.py to match the following code block
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
````

</details>
