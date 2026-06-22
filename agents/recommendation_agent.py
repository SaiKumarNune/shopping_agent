from pathlib import Path

from langchain_groq import ChatGroq

from utils.config import GROQ_API_KEY, GROQ_MODEL


PROMPT_PATH = (
    Path(__file__).parent.parent
    / "prompts"
    / "recommendation_agent_prompt.txt"
)

SYSTEM_PROMPT = PROMPT_PATH.read_text()


llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=GROQ_MODEL,
    temperature=0
)


def recommendation_agent(state: dict):
    user_query = state["user_query"]
    products = state.get("products", [])
    route = state.get("route", "general")

    if not products:
        if route == "general":
            prompt = f"""
You are a helpful AI shopping assistant.

The user asked a general question, not a product database search question.

User question:
{user_query}

Answer naturally. If the question is outside shopping, still answer briefly and politely.
"""
            response = llm.invoke(prompt)

            return {
                **state,
                "final_answer": response.content
            }

        return {
            **state,
            "final_answer": "I could not find matching products in the database."
        }

    products_text = ""

    for product in products:
        products_text += f"""
Product ID: {product['id']}
Name: {product['name']}
Category: {product['category']}
Price: ${product['price']}
Organic: {"Yes" if product['is_organic'] else "No"}
Stock: {product['stock']}
Average Rating: {product.get('average_rating', 'N/A')}
Description: {product['description']}
"""

    prompt = f"""
{SYSTEM_PROMPT}

User request:
{user_query}

Available products:
{products_text}
"""

    response = llm.invoke(prompt)

    return {
        **state,
        "final_answer": response.content
    }