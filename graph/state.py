from typing import TypedDict

class CustomerSupportState(TypedDict):
    customer_name: str
    query: str
    intent: str
    retrieved_context: str
    approval_required: bool
    approval_status: str
    response: str