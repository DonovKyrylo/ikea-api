from enum import Enum
from pydantic import BaseModel

class Color(Enum):
    WHITE: str


class Product(BaseModel):
    name: str
    url: str
    imageUrl: str
    price: float
