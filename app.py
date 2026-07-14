import gradio as gr
from vector_DB import build_vector_store
from rag_chat import chat

# Store vector database globally
vector_db = None

def process_video(url):
    
    global vector_db

    if not url.strip():
        return "❌ Please enter a YouTube URL."

    try:
        vector_db = build_vector_store(url)

        if vector_db is None:
            return "❌ Failed to process video."

        return "✅ Video processed successfully!"

    except Exception as e:
        return f"❌ Error:\n{e}"


def ask_question(question):
    global vector_db

    if vector_db is None:
        return "Please process a YouTube video first."

    if not question.strip():
        return "Please enter a question."

    try:
        answer = chat(question, vector_db)

        if answer is None:
            return "No answer found."

        return answer

    except Exception as e:
        return str(e)


with gr.Blocks(title="YouTube Video Retriever") as demo:

    gr.Markdown("# 🎥 YouTube Video Retriever")

    with gr.Row():
        url = gr.Textbox(
            label="YouTube URL",
            placeholder="Paste YouTube URL..."
        )

    process_btn = gr.Button("Process Video")

    status = gr.Textbox(
        label="Status",
        interactive=False
    )

    process_btn.click(
        fn=process_video,
        inputs=url,
        outputs=status
    )

    gr.Markdown("---")

    question = gr.Textbox(
        label="Ask Question",
        placeholder="Ask anything about the video..."
    )

    ask_btn = gr.Button("Ask")

    answer = gr.Textbox(
        label="Answer",
        lines=10
    )

    ask_btn.click(
        fn=ask_question,
        inputs=question,
        outputs=answer
    )

demo.launch(server_name="0.0.0.0",
            server_port=7860,
            show_error=True
           )
