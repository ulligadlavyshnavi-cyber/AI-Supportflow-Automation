from graph.state import CustomerSupportState

def classify_intent(state: CustomerSupportState):

    query = state["query"].lower()

    # Billing first
    if any(word in query for word in ["refund", "invoice", "payment", "billing"]):
        state["intent"] = "billing"

    # Sales
    elif any(word in query for word in ["price", "pricing", "plan", "subscription"]):
        state["intent"] = "sales"

    # Account
    elif any(word in query for word in ["password", "login", "profile", "account"]):
        state["intent"] = "account"

    # Technical
    elif any(word in query for word in ["error", "crash", "install", "configuration", "upload"]):
        state["intent"] = "technical"

    # Memory
    elif "previous" in query:
        state["intent"] = "memory"

    else:
        state["intent"] = "unknown"

    return state