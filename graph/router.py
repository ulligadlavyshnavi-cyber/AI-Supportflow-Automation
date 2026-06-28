from graph.state import CustomerSupportState

def route_query(state: CustomerSupportState):

    intent = state["intent"]

    if intent == "sales":
        return "sales_agent"

    elif intent == "technical":
        return "technical_agent"

    elif intent == "billing":
        return "billing_agent"

    elif intent == "account":
        return "account_agent"

    elif intent == "memory":
        return "memory_agent"

    return "supervisor_agent"