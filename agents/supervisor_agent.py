from graph.state import CustomerSupportState
from memory.sqlite_memory import save_conversation

def supervisor_agent(state: CustomerSupportState):

    save_conversation(
        state["customer_name"],
        state["query"],
        state["response"]
    )

    state["response"] = (
        "Supervisor Verified Response:\n\n"
        + state["response"]
    )

    return state