import gradio as gr
from fastapi import FastAPI
from main import ask_tableau_agent

app = FastAPI(title="AI Analytics Agent")

def gradio_ask(question):
    return ask_tableau_agent(question)


with gr.Blocks(theme=gr.themes.Soft()) as gradio_ui:
    gr.Markdown(
        """
        # AI Analytics Agent (Conversational Analytics)
        Interact with a published dataset on Tableau **SuperStore** dataset using natural language (a LLM analytics application)

        **Examples you can try:** 
        - Top customers by profit  
        - Sales trend by category  
        """
    )

    with gr.Row():
        question_input = gr.Textbox(
            label="Your Question",
            placeholder="e.g. Show total profit for the last year",
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
        "message": "AI Analytics Agent is running"
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
