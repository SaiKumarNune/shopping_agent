import re
from tools.product_tools import search_products


PRODUCT_WORDS = [
    "honey", "tea", "milk", "oats", "peanut butter",
    "product", "products", "item", "items", "recommend",
    "find", "show", "buy", "under", "organic"
]

FOLLOW_UP_WORDS = [
    "which one", "highest rating", "cheapest", "best one",
    "compare", "among these", "from these", "why", "that one",
    "it", "this", "better"
]


def is_follow_up_question(user_query: str):
    query = user_query.lower()
    return any(word in query for word in FOLLOW_UP_WORDS)


def is_product_question(user_query: str):
    query = user_query.lower()
    return any(word in query for word in PRODUCT_WORDS)


def extract_max_price(user_query: str):
    numbers = re.findall(r"\d+", user_query)
    if numbers:
        return float(numbers[-1])
    return None


def extract_product_query(user_query: str):
    query = user_query.lower()

    remove_words = [
        "find", "show", "me", "best", "recommend", "under", "below",
        "less", "than", "between", "dollars", "dollar", "$", "organic",
        "buy", "products", "product", "items", "item"
    ]

    for word in remove_words:
        query = query.replace(word, "")

    query = re.sub(r"\d+", "", query)
    query = query.strip()

    return query


def search_agent(state: dict):
    user_query = state["user_query"]
    previous_products = state.get("previous_products", [])

    if previous_products and is_follow_up_question(user_query):
        return {
            **state,
            "product_query": "follow-up question",
            "max_price": None,
            "products": previous_products,
            "route": "follow_up"
        }

    if not is_product_question(user_query):
        return {
            **state,
            "product_query": "general question",
            "max_price": None,
            "products": [],
            "route": "general"
        }

    product_query = extract_product_query(user_query)
    max_price = extract_max_price(user_query)

    products = search_products(product_query, max_price)

    return {
        **state,
        "product_query": product_query,
        "max_price": max_price,
        "products": products,
        "route": "product_search"
    }