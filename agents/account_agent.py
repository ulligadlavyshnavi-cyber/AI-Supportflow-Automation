from graph.state import CustomerSupportState
from rag.retriever import retrieve_context

def account_agent(state: CustomerSupportState):

    context = retrieve_context(state["query"])

    state["retrieved_context"] = context

    state["response"] = (
        "Account Support\n\n"
        + context
    )

    return state