from workflows.shopping_graph import run_shopping_workflow


if __name__ == "__main__":
    user_query = input("Ask your shopping question: ")

    result = run_shopping_workflow(user_query)

    print("\n=== Search Results ===")
    for product in result["products"]:
        print(product)

    print("\n=== Final Recommendation ===")
    print(result["final_answer"])