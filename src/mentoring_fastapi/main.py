from fastapi import FastAPI

from mentoring_fastapi import schemas

app = FastAPI()


@app.get("/echo/{name}")
async def echo(name: str) -> schemas.EchoResponse:
    return schemas.EchoResponse(greeting=f"Hello {name}!")
