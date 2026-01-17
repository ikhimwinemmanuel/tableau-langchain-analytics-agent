## Tableau LangChain Analytics Agent

A data-grounded natural language analytics service that allows users to ask questions in plain English and receive answers directly from governed Tableau Cloud data sources — without writing SQL or building dashboards.

This project explores how Large Language Models (LLMs) can be used responsibly as an orchestration layer on top of trusted analytics systems, rather than as standalone answer generators.

---

## Overview

This project implements an end-to-end **Natural Language Query (NLQ)** system on top of **Tableau Cloud**.

Instead of relying on an LLM’s internal knowledge, all responses are generated only after querying a published Tableau data source via LLM-initiated tool calls. The LLM functions strictly as a reasoning and orchestration layer — deciding when and how to invoke governed Tableau query tools

If a question cannot be answered from the connected Tableau datasource, the system **fails gracefully rather than hallucinating results**.

This implementation uses the **Tableau Superstore** dataset as a safe, non-sensitive demonstration datasource.

---

## Tech Stack

- **Python** – core implementation  
- **FastAPI** – backend API layer  
- **LangChain** – LLM orchestration and agent logic  
- **LangGraph** – ReAct-style agent execution  
- **LangSmith** – agent tracing, debugging, and observability  
- **Tableau Cloud** – governed analytics backend  
- **Tableau Connected Apps (JWT)** – secure authentication  
- **OpenAI** – LLM provider (model-agnostic design)  
- **Hugging Face Spaces** – public deployment  

---

## Architecture Summary

### Query Flow

1. User submits a natural-language question  
2. FastAPI receives the request  
3. LangChain agent interprets user intent  
4. The agent invokes Tableau query tools  
5. Tableau Cloud executes governed queries  
6. Results are returned to the LLM  
7. The LLM summarizes results into a human-readable response  
8. A data-grounded answer is returned via the API  

Importantly, **the LLM does not invent metrics or values** — it only reasons over retrieved Tableau results.

---

## Project Structure
```
tableau-langchain-analytics-agent/
├── main.py                      # Core LangChain + Tableau agent logic
├── api.py                       # FastAPI service layer
├── utilities/
│   ├── prompt.py                # Agent identity and system prompts
│   ├── chat.py                  # Response handling utilities
│   └── find_datasource_luid_gql.py  # Retrieve datasource LUID via GraphQL
├── requirements.txt             # Python dependencies
├── .gitignore                   # Excludes secrets and virtual environments
└── README.md                    # Project documentation
```
---

## Deployment

The application is containerized using **Docker** and deployed on **Hugging Face Spaces**.

- All environment variables and secrets were securely stored in the Hugging Face environment variable and secret store.
- No credentials are hard-coded  
- Tableau access is secured via JWT-based Connected Apps  

---

## Key Design Principles

- **Data grounding over generation**  
- **Governed analytics first**  
- **LLMs as orchestration layers, not analytics engines**  
- **Security and access control by design(JWT)**  

---

## License

MIT

## Live Demo

Try the live application on Hugging Face Spaces:

https://ikhimwin-tableau-langchain-analytics-agent.hf.space/ui/ 

## Publication on Medium

https://medium.com/@ikhimwinemmanuel/building-a-data-grounded-genai-analytics-application-with-tableau-and-langchain-e407b68bf9e3
