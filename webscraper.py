from enum import Enum
from requests import get

class Color(Enum):
    WHITE: str



def search_request(q: str, **kwargs: str):
    return get(
        f"https://sik.search.blue.cdtapps.com/it/it/search-result-page?q={q}&"
        + "&".join(f"{key}={value}" for key, value in kwargs.items())
    ).json()["searchResultPage"]["products"]["main"]["items"]

print(search_request("scaffale", page="2"))
