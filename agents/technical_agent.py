from graph.state import CustomerSupportState

def technical_agent(state: CustomerSupportState):

    state["response"] = """
We understand you are facing a technical issue.

Please follow these steps:

1. Restart the application.
2. Update to the latest version.
3. Check your internet connection.

For more details, refer to the Technical Manual.
"""

    return state 