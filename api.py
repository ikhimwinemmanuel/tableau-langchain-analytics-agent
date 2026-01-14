import gradio as gr
from fastapi import FastAPI
from main import ask_tableau_agent

app = FastAPI(title="Tableau LangChain Analytics Agent")

def gradio_ask(question):
    return ask_tableau_agent(question)


with gr.Blocks(theme=gr.themes.Soft()) as gradio_ui:
    gr.Markdown(
        """
        # 📊 Tableau LangChain Analytics Agent  
        Ask natural-language questions over your Tableau **Superstore** data.

        **Examples you can try:**
        - Show total sales by region  
        - Top customers by profit  
        - Sales trend by category  
        """
    )

    with gr.Row():
        question_input = gr.Textbox(
            label="Your Question",
            placeholder="e.g. Show total sales by region",
            lines=2
        )

    ask_button = gr.Button("Run Analysis", variant="primary")

    answer_output = gr.Textbox(
        label="Answer",
        lines=8,
        interactive=False
    )

    ask_button.click(
        fn=gradio_ask,
        inputs=question_input,
        outputs=answer_output
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
