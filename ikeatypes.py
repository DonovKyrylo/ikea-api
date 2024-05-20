from enum import Enum
from pydantic import BaseModel

class Color(Enum):
    WHITE = 10156
    BLACK = 10139
    BEIGE = 10003
    BROWN = 10019
    GREY = 10028
    GRAY = GREY
    RED = 10124
    YELLOW = 10042
    GREEN = 10033
    BLUE = 10007
    PINK = 10119
    ORANGE = 10112
    LILAC = 10064
    PURPLE = LILAC
    TURQUOISE = 10152
    CYAN = TURQUOISE
    LIGHT_BLUE = TURQUOISE
    FANTASY = 10583
    MULTICOLOR = FANTASY

class SortType(Enum):
    RELEVANCE = "RELEVANCE"
    PRICE_LOW_TO_HIGH = "PRICE_LOW_TO_HIGH"
    PRICE_HIGH_TO_LOW = "PRICE_HIGH_TO_LOW"
    NEWEST = "NEWEST"
    RATING = "RATING"
    NAME_ASCENDING = "NAME_ASCENDING"
    MOST_POPULAR = "MOST_POPULAR"
    WIDTH = "WIDTH"
    HEIGHT = "HEIGHT"
    LENGTH = "LENGTH"

class Product(BaseModel):
    name: str
    url: str
    imageUrl: str
    price: float
