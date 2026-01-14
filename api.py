import gradio as gr
from fastapi import FastAPI
from main import ask_tableau_agent

app = FastAPI(title="Tableau LangChain Analytics Agent")

def gradio_ask(question):
    return ask_tableau_agent(question)

gradio_ui = gr.Interface(
    fn=gradio_ask,
    inputs=gr.Textbox(
        label="Ask a Tableau question",
        placeholder="e.g. Show total sales by region"
    ),
    outputs=gr.Textbox(label="Answer"),
    title="Tableau LangChain Analytics Agent",
    description="Ask natural-language questions over Tableau data using LangChain."
)


@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Tableau LangChain Analytics Agent is running"
    }



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


app = gr.mount_gradio_app(app, gradio_ui, path="/ui")
