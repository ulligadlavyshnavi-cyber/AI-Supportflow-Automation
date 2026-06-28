# AI-Powered Customer Support Automation System

## Project Overview

This project is an AI-powered customer support automation system developed using LangGraph. It automates customer support by classifying customer queries, routing them to the appropriate department, retrieving information using RAG, storing conversation history in SQLite, handling human approval for sensitive requests, and generating final responses.

---

## Features

- Intent Classification
- Conditional Routing
- Sales Support Agent
- Technical Support Agent
- Billing Support Agent
- Account Support Agent
- Retrieval-Augmented Generation (RAG)
- SQLite Memory
- Human-in-the-Loop Approval
- Supervisor Agent
- Final Response Generation

---

## Technologies Used

- Python
- LangGraph
- LangChain
- HuggingFace Embeddings
- FAISS
- SQLite
- VS Code
- GitHub Codespaces

---

## Project Structure

```
AI-Supportflow-Automation
│
├── agents
├── graph
├── memory
├── rag
├── documents
├── screenshots
├── workflow
├── app.py
├── requirements.txt
├── README.md
└── memory.db
```

---

## Workflow

Customer Query

↓

Intent Classification

↓

Conditional Routing

↓

Support Agent

↓

RAG Retrieval

↓

Human Approval (if required)

↓

Supervisor Agent

↓

SQLite Memory

↓

Final Response

---

## Sample Queries

1. What are the pricing plans available for your software?
2. I forgot my account password.
3. My application crashes whenever I upload a file.
4. I need a refund for my annual subscription.
5. What was my previous support issue?

---