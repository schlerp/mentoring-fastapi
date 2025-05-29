import pydantic


class EchoResponse(pydantic.BaseModel):
    greeting: str
