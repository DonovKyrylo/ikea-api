from requests import get
from pprint import pprint
from ikeatypes import *


def search_request(q: str, **kwargs: str):
    items = get(
        f"https://sik.search.blue.cdtapps.com/it/it/search-result-page?q={q}&"
        + "&".join(f"{key}={value}" for key, value in kwargs.items())
    ).json()["searchResultPage"]["products"]["main"]["items"]

    products: list[Product] = []
    for item in items:
        product = item.get("product") or item.get("featuredProduct")
        if product:
            products.append(
                Product(
                    name=product["name"],
                    url=product["pipUrl"],
                    imageUrl=product["mainImageUrl"],
                    price=product["salesPrice"]["numeral"]
                )
            )

    return products

pprint(search_request("scaffale"))
