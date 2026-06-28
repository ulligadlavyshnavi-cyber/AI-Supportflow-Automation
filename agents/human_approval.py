from graph.state import CustomerSupportState

def human_approval(state: CustomerSupportState):

    risky_keywords = [
        "refund",
        "cancel",
        "closure",
        "compensation",
        "management"
    ]

    query = state["query"].lower()

    if any(word in query for word in risky_keywords):

        state["approval_required"] = True

        print("\nHuman Approval Required")

        decision = input("Approve Request? (yes/no): ")

        state["approval_status"] = decision

    else:

        state["approval_required"] = False

        state["approval_status"] = "Approved"

    return state