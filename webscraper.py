from requests import get
from ikeatypes import *
import logging

logger = logging.getLogger("uvicorn.info")

def remove_null_params(params: dict[str]):
    return {key: value for key, value in params.items() if value != None}

def search_request(
        query: str = None,
        locale: Locale = Locale.EN_US,
        color: Color = None,
        sort: SortType = SortType.RELEVANCE,
        includeFeatured = False
    ) -> list[Product]:

    url = f"https://sik.search.blue.cdtapps.com/{locale.value[3:]}/{locale.value[:2]}/search-result-page"
    params = remove_null_params({
        "q": query,
        "f-colors": color.value if color != None else None,
        "sort": sort.value if sort != None else None
    })

    logger.info(f"Sending request to {url} with params: {params}")

    request_result = get(url, params).json()

    items = request_result["searchResultPage"]["products"]["main"]["items"]

    products: list[Product] = []
    for item in items:

        product = item.get("product")
        isFeatured = False


        if includeFeatured and product is None:
            product = item.get("featuredProduct")
            isFeatured = True

        if product:
            products.append(
                Product(
                    name=product["name"],
                    typeName=product["typeName"],
                    url=product["pipUrl"],
                    imageUrl=product["mainImageUrl"],
                    itemMeasure=product["itemMeasureReferenceText"],
                    price=ProductPrice(
                        value=product["salesPrice"]["numeral"],
                        currencySymbol=product["salesPrice"]["current"]["prefix"]
                    ),
                    isFeatured=isFeatured
                )
            )

    return products
