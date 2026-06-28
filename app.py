from graph.workflow import graph

def main():

    print("=" * 60)
    print("AI Powered Customer Support Automation System")
    print("=" * 60)

    customer_name = input("Enter Customer Name: ")
    query = input("Enter Customer Query: ")

    state = {
        "customer_name": customer_name,
        "query": query,
        "intent": "",
        "retrieved_context": "",
        "approval_required": False,
        "approval_status": "",
        "response": ""
    }

    result = graph.invoke(state)

    print("\nFinal Response")
    print("-" * 40)
    print(result["response"])


if __name__ == "__main__":
    main()