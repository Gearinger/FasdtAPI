from pydantic import BaseModel
from typing import Optional


class NamePassword(BaseModel):
    title: str
    name: str
    password: str
    url: Optional[str] = None
    bz: Optional[str] = None
