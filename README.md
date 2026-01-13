## Tableau LangChain Analytics Agent

A natural language analytics service that enables users to ask questions in plain English and receive data-grounded answers directly from Tableau Cloud data sources, without writing SQL or building dashboards.

Built as a practical exploration of LLM-powered analytics, LangChain tool orchestration, and secure enterprise data access via Tableau Connected Apps.

## Overview

This project implements an end-to-end Natural Language Query (NLQ) system on top of Tableau Cloud.

Instead of relying on an LLM’s internal knowledge, all answers are generated only after querying a published Tableau data source. The LLM acts purely as a reasoning layer that decides how to query the data, not what the data is.

If a question cannot be answered from the connected Tableau datasource, the system fails gracefully rather than hallucinating results.

The initial implementation uses the Tableau Superstore dataset as a safe, non-sensitive demo datasource.

## Tech Stack

Python – core implementation

FastAPI – backend API layer

LangChain – LLM orchestration and agent logic

LangGraph – ReAct-style agent execution

Tableau Cloud – trusted analytics data source

Tableau Connected Apps (JWT) – secure authentication

OpenAI – LLM backend (switchable)

Hugging Face Spaces – for public deployment

## Architecture Summary
Query Flow

User submits a natural language question

FastAPI receives the request

LangChain agent interprets the question

Agent invokes Tableau query tools

Tableau Cloud returns structured results

LLM summarizes results into a human-readable answer

API returns a grounded response

## Structure 

tableau-langchain-analytics-agent/
├── main.py                            # Core LangChain + Tableau agent logic
├── api.py                             # FastAPI service layer
├── utilities/
│   ├── prompt.py                      # Agent identity and system prompts
│   ├── chat.py                        # Response handling utilities
│   └── find_datasource_luid_gql.py    # To extract luid from Datasource
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Excludes secrets and virtual environments
└── README.md                          # Project documentation






