from fastapi import FastAPI
import pydantic

app = FastAPI()


class EchoResponse(pydantic.BaseModel):
    greeting: str


@app.get("/echo/{name}")
async def echo(name: str) -> EchoResponse:
    return EchoResponse(greeting=f"Hello {name}!")
