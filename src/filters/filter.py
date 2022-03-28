from pydantic import BaseModel


class Filter(BaseModel):
    name: str = "base"
    filter: str = None
