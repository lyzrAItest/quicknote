import streamlit as st
import requests
import os

def get_support_response(query: str, username: str) -> str:
    """
    Returns a static response to a user query based on keywords, personalized with the username.
    """
    prompt = f"Username: {username}/n/n User-Query: {query}"
    prompt+=f"Github url: https://github.com/Rakshith176/targaryen"

    lyzr_api = "https://agent-prod.studio.lyzr.ai/v3/inference/chat/"

    headers = {
        'x-api-key': 'sk-default-UZ8vuAEqinaiNcC8Qc9xS64h90Qe5uLg'
    }

    # The payload as a Python dictionary
    payload = {
        "user_id": "test1@vikrams.in",
        "agent_id": "6857c7cd8da27df0ba09d552",
        "session_id": "6857c7cd8da27df0ba09d552-mbxn6looxu",
        "message": prompt
    }

    response = requests.post(lyzr_api, headers=headers, json=payload)
    # response['messages']
    return response.json()['response']

def support_page():
    """
    Renders the Support Agent chat page.
    """
    st.header("Support Agent")
    st.write(f"Welcome, {st.session_state.username}. Ask a question about using the app.")

    if st.button("← Back to Notes"):
        st.session_state.page = "list"
        if "support_messages" in st.session_state:
            del st.session_state.support_messages
        st.rerun()

    # Initialize chat history
    if "support_messages" not in st.session_state:
        st.session_state.support_messages = [{"role": "assistant", "content": "How can I help you today?"}]

    # Display chat messages
    for message in st.session_state.support_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept and process user input
    if prompt := st.chat_input("Ask me anything..."):
        # Display user message and add to history
        st.chat_message("user").markdown(prompt)
        st.session_state.support_messages.append({"role": "user", "content": prompt})

        # Get and display assistant response
        response = get_support_response(prompt, st.session_state.username)
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.support_messages.append({"role": "assistant", "content": response}) 