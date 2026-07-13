import streamlit as st

from vector_DB import build_vector_store
from rag_chat import chat

st.set_page_config(
    page_title="YouTube Retriever",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 YouTube Video Retriever")

url = st.text_input("Enter YouTube URL")

if st.button("Process Video"):

    if url.strip() == "":
        st.warning("Please enter a YouTube URL.")

    else:

        try:

            with st.spinner("Processing video..."):

                vector_db = build_vector_store(url)

                st.session_state["vector_db"] = vector_db

            st.success("Video processed successfully!")

        except Exception as e:

            st.error(f"Error: {e}")

if "vector_db" in st.session_state:

    st.divider()

    st.subheader("Ask Questions")

    question = st.text_input("Enter your question")

    if st.button("Ask"):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            with st.spinner("Generating answer..."):

                answer = chat(
                    question,
                    st.session_state["vector_db"]
                )

            st.write("### Answer")

            st.write(answer)