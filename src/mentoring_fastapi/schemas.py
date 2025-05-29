import datetime
import typing

import pydantic


class OrmBaseModel(pydantic.BaseModel):
    """
    Base model for ORM objects to enable ORM mode.

    NOTE: ORM mode has been renamed to `from_attributes` in Pydantic v2.
    """

    model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
        from_attributes=True,
    )


class EchoResponse(OrmBaseModel):
    greeting: str
