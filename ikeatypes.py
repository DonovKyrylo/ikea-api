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

class Locale(Enum):
    AR_BH = "ar-bh"
    AR_EG = "ar-eg"
    AR_JO = "ar-jo"
    AR_KW = "ar-kw"
    AR_MA = "ar-ma"
    AR_OM = "ar-om"
    AR_QA = "ar-qa"
    AR_SA = "ar-sa"
    AR_AE = "ar-ae"
    EU_ES = "eu-es"
    CA_ES = "ca-es"
    ZH_CN = "zh-cn"
    HR_HR = "hr-hr"
    CS_CZ = "cs-cz"
    DA_DK = "da-dk"
    NL_BE = "nl-be"
    NL_NL = "nl-nl"
    EN_AU = "en-au"
    EN_AT = "en-at"
    EN_BE = "en-be"
    EN_CA = "en-ca"
    EN_FI = "en-fi"
    EN_DE = "en-de"
    EN_IN = "en-in"
    EN_IE = "en-ie"
    EN_MY = "en-my"
    EN_NL = "en-nl"
    EN_PH = "en-ph"
    EN_SG = "en-sg"
    EN_SE = "en-se"
    EN_CH = "en-ch"
    EN_AE = "en-ae"
    EN_GB = "en-gb"
    EN_US = "en-us"
    FI_FI = "fi-fi"
    FR_BE = "fr-be"
    FR_CA = "fr-ca"
    FR_FR = "fr-fr"
    FR_MA = "fr-ma"
    FR_CH = "fr-ch"
    GL_ES = "gl-es"
    DE_AT = "de-at"
    DE_DE = "de-de"
    DE_CH = "de-ch"
    HE_IL = "he-il"
    HU_HU = "hu-hu"
    IT_IT = "it-it"
    IT_CH = "it-ch"
    JA_JP = "ja-jp"
    KO_KR = "ko-kr"
    MS_MY = "ms-my"
    PL_PL = "pl-pl"
    PT_PT = "pt-pt"
    RO_RO = "ro-ro"
    RU_RU = "ru-ru"
    SK_SK = "sk-sk"
    SL_SI = "sl-si"
    ES_CL = "es-cl"
    ES_CO = "es-co"
    ES_MX = "es-mx"
    ES_ES = "es-es"
    SV_SE = "sv-se"
    TH_TH = "th-th"
    UK_UA = "uk-ua"

    
class Product(BaseModel):
    name: str
    typeName: str
    url: str
    imageUrl: str
    itemMeasure: str
    price: 'ProductPrice'
    isFeatured: bool

class ProductPrice(BaseModel):
    value: float
    currencySymbol: str
