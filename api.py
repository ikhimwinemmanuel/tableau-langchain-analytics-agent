from fastapi import FastAPI
from main import ask_tableau_agent

app = FastAPI(title="Tableau LangChain Analytics Agent")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/ask")
def ask(question: str):
    answer = ask_tableau_agent(question)
    return {
        "question": question,
        "answer": answer
    }
