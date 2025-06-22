import streamlit as st
import json

def verify_user(username, password):
    """
    Verifies user credentials against the users.json file.
    """
    try:
        # with open("frontend/users.json", "r") as f:
        #     users = json.load(f)
        # for user in users:
        #     if user["username"] == username and user["password"] == password:
        return True
    except FileNotFoundError:
        st.error("users.json not found. Please create it.")
        return False
    return False

def login_page():
    """
    Renders the login page and handles user authentication.
    """
    st.header("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if verify_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Logged in successfully!")
            st.rerun()
        else:
            st.error("Invalid username or password.") 