from pydantic import BaseModel


class Supplier(BaseModel):
    id: str
    name: str
