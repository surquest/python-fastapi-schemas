from pydantic import Field
# from pydantic import BaseModel
from .base import Base
from typing import Optional


class Message(Base):

    msg: str = Field(...)
    type: Optional[str] = None
    loc: Optional[list] = None
    ctx: Optional[dict] = None
