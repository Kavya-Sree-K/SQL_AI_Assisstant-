import streamlit as st
import pandas as pd
import os

from sql_agent import ask_database
from query_logger import log_query
from database import db

st.set_page_config(
    page_title="SQL AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 SQL AI Assistant")
st.caption("Natural Language to SQL using Gemini + LangChain")

# Session State

if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar

with st.sidebar:

    st.header("Database Assistant")

    st.success("Connected to MySQL")

    st.markdown("---")

    st.subheader("Example Questions")

    st.write("• List comedy movies")
    st.write("• Show top rated movies")
    st.write("• Count movies by genre")
    st.write("• Movies released after 2020")

    st.markdown("---")

    # Schema Viewer

    if st.checkbox("Show Database Schema"):

        st.code(
            db.get_table_info()
        )

    st.markdown("---")

    # Analytics

    if st.checkbox("Analytics Dashboard"):

        if os.path.exists("logs/queries.csv"):

            df = pd.read_csv(
                "logs/queries.csv"
            )

            st.metric(
                "Total Queries",
                len(df)
            )

            st.dataframe(df)

    st.markdown("---")

    # Download Logs

    if os.path.exists(
        "logs/queries.csv"
    ):

        with open(
            "logs/queries.csv",
            "rb"
        ) as file:

            st.download_button(
                label="Download Query Logs",
                data=file,
                file_name="query_logs.csv",
                mime="text/csv"
            )

    st.markdown("---")

    if st.button("Clear Chat"):

        st.session_state.messages = []
        st.rerun()

# Display Chat

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

# User Input

question = st.chat_input(
    "Ask any database question..."
)

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.spinner(
        "Analyzing Database..."
    ):

        try:

            response = ask_database(
                question
            )

            answer = response["output"]

            st.session_state.messages.append(
                {
                    "role":"assistant",
                    "content":answer
                }
            )

            log_query(
                question,
                answer
            )

            with st.chat_message(
                "assistant"
            ):

                st.markdown(answer)

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )