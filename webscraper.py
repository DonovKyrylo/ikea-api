from requests import get
from ikeatypes import *

def remove_null_params(params: dict[str]):
    return {key: value for key, value in params.items() if value != None}

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

