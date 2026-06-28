from graph.state import CustomerSupportState
from rag.retriever import retrieve_context

def billing_agent(state: CustomerSupportState):

    context = retrieve_context(state["query"])

    state["retrieved_context"] = context

    state["response"] = (
        "Billing Support\n\n"
        + context
    )

    return state