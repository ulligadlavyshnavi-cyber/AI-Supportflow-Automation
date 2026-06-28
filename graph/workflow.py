from langgraph.graph import StateGraph, END

from graph.state import CustomerSupportState
from graph.router import route_query

from agents.intent_classifier import classify_intent
from agents.sales_agent import sales_agent
from agents.technical_agent import technical_agent
from agents.billing_agent import billing_agent
from agents.account_agent import account_agent
from agents.human_approval import human_approval
from agents.supervisor_agent import supervisor_agent 
from agents.memory_agent import memory_agent
workflow = StateGraph(CustomerSupportState) 
workflow.add_node("intent_classifier", classify_intent)
workflow.add_node("sales_agent", sales_agent)
workflow.add_node("technical_agent", technical_agent)
workflow.add_node("billing_agent", billing_agent)
workflow.add_node("account_agent", account_agent)
workflow.add_node("human_approval", human_approval)
workflow.add_node("supervisor_agent", supervisor_agent) 
workflow.add_node("memory_agent", memory_agent)
workflow.set_entry_point("intent_classifier") 
workflow.add_conditional_edges(
    "intent_classifier",
    route_query,
    {
        "sales_agent": "sales_agent",
        "technical_agent": "technical_agent",
        "billing_agent": "billing_agent",
        "account_agent": "account_agent",
        "memory_agent": "memory_agent"
    }
)
workflow.add_edge("sales_agent", "supervisor_agent")
workflow.add_edge("technical_agent", "supervisor_agent")
workflow.add_edge("account_agent", "supervisor_agent")

workflow.add_edge("billing_agent", "human_approval")
workflow.add_edge("human_approval", "supervisor_agent")
workflow.add_edge("supervisor_agent", END)
workflow.add_edge("memory_agent", END)
graph = workflow.compile() 