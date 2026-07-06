import requests
import streamlit as st

BACKEND_URL = "http://backend:8000/api/v2/chat"

st.set_page_config(
    page_title="Enterprise AI Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Enterprise AI Agent")

st.caption("Ask questions about your organization's documents.")

question = st.text_area(
    "Question",
    height=120
)

if st.button("Ask AI", use_container_width=True):

    if question.strip():

        with st.spinner("Searching documents and generating answer..."):

            try:

                response = requests.post(
                    BACKEND_URL,
                    json={
                        "message": question,
                        "session_id": "streamlit"
                    },
                    timeout=300
                )

                response.raise_for_status()

                answer = response.json()

                st.success("Answer")

                st.write(answer["response"])

            except Exception as e:

                st.error(str(e))