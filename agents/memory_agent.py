from graph.state import CustomerSupportState
from memory.sqlite_memory import get_previous_issue

def memory_agent(state: CustomerSupportState):

    previous = get_previous_issue(state["customer_name"])

    state["response"] = (
        f"Your previous support issue was:\n\n{previous}"
    )

    return state