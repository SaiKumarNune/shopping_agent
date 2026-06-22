import streamlit as st
from workflows.shopping_graph import run_shopping_workflow


st.set_page_config(
    page_title="Multi-Agent Shopping Assistant",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Multi-Agent Shopping Assistant")

st.caption("LangGraph + Search Agent + Recommendation Agent + SQLite + Groq")


if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_products" not in st.session_state:
    st.session_state.last_products = []


with st.sidebar:
    st.header("Architecture")

    st.markdown("""
    **Workflow**
    
    User → Search Agent → Product DB → Recommendation Agent → Answer

    **Supports**
    - Product search
    - Price filtering
    - Recommendations
    - Follow-up context
    """)

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.session_state.last_products = []
        st.rerun()


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_question = st.chat_input("Ask something like: Find organic honey under $15")


if user_question:
    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )

    with st.chat_message("user"):
        st.markdown(user_question)

    previous_context = ""

    if st.session_state.last_products:
        previous_context += "\nPrevious retrieved products:\n"

        for product in st.session_state.last_products:
            previous_context += (
                f"- {product['name']} | "
                f"Price: ${product['price']} | "
                f"Rating: {product.get('average_rating', 'N/A')} | "
                f"Organic: {'Yes' if product['is_organic'] else 'No'}\n"
            )

    full_question = f"""
Previous context:
{previous_context}

Current user question:
{user_question}
"""

    with st.chat_message("assistant"):
        with st.spinner("Running multi-agent workflow..."):
            result = run_shopping_workflow(
                user_question,
                previous_products=st.session_state.last_products
            )

        answer = result.get("final_answer", "No answer generated.")

        st.markdown(answer)

        with st.expander("View Search Agent Results"):
            products = result.get("products", [])

            if products:
                for product in products:
                    st.markdown(
                        f"""
                        **{product['name']}**
                        - Price: ${product['price']}
                        - Rating: {product.get('average_rating', 'N/A')}
                        - Organic: {'Yes' if product['is_organic'] else 'No'}
                        - Stock: {product['stock']}
                        - Description: {product['description']}
                        """
                    )
            else:
                st.write("No products retrieved.")

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    if result.get("products"):
        st.session_state.last_products = result["products"]