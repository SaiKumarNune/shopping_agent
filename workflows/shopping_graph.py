from typing import TypedDict, List, Optional
from langgraph.graph import StateGraph, END

from agents.search_agent import search_agent
from agents.recommendation_agent import recommendation_agent


class ShoppingState(TypedDict):
    user_query: str
    product_query: Optional[str]
    max_price: Optional[float]
    products: List[dict]
    previous_products: List[dict]
    final_answer: Optional[str]
    route: Optional[str]


def build_shopping_graph():
    graph = StateGraph(ShoppingState)

    graph.add_node("search_agent", search_agent)
    graph.add_node("recommendation_agent", recommendation_agent)

    graph.set_entry_point("search_agent")

    graph.add_edge("search_agent", "recommendation_agent")
    graph.add_edge("recommendation_agent", END)

    return graph.compile()


def run_shopping_workflow(user_query: str, previous_products=None):
    app = build_shopping_graph()

    initial_state = {
        "user_query": user_query,
        "product_query": None,
        "max_price": None,
        "products": [],
        "previous_products": previous_products or [],
        "final_answer": None,
        "route": None,
    }

    result = app.invoke(initial_state)
    return result