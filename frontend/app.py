import streamlit as st
import requests
from support import support_page
from login import login_page

# --- API Configuration ---
API_URL = "http://127.0.0.1:8000"

# --- API Client ---
def get_notes():
    try:
        res = requests.get(f"{API_URL}/notes")
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching notes: {e}")
        return []

def get_note(note_id):
    try:
        res = requests.get(f"{API_URL}/notes/{note_id}")
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching note: {e}")
        return None

def create_note(title, content):
    note_data = {"title": title, "content": content}
    try:
        res = requests.post(f"{API_URL}/notes", json=note_data)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error creating note: {e}")
        return None

def update_note(note_id, title, content):
    note_data = {"title": title, "content": content}
    try:
        res = requests.put(f"{API_URL}/notes/{note_id}", json=note_data)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error updating note: {e}")
        return None

def delete_note(note_id):
    try:
        res = requests.delete(f"{API_URL}/notes/{note_id}")
        res.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        st.error(f"Error deleting note: {e}")
        return False

# --- UI Components ---
def note_editor_screen():
    st.header("Note Editor")

    note_id = st.session_state.get("current_note_id")
    note = st.session_state.get("current_note")

    title = st.text_input("Title", value=note["title"] if note else "")
    content = st.text_area("Content", value=note["content"] if note else "", height=300)

    col1, col2, col3 = st.columns([1,1,3])

    with col1:
        if st.button("Save"):
            if not title:
                st.warning("Title cannot be empty.")
                return

            if note_id: # Update existing note
                update_note(note_id, title, content)
            else: # Create new note
                create_note(title, content)
            
            st.session_state.page = "list"
            st.rerun()

    with col2:
        if note_id:
            if "delete_confirm" not in st.session_state:
                st.session_state.delete_confirm = False

            if st.button("Delete"):
                st.session_state.delete_confirm = True
            
            if st.session_state.delete_confirm:
                st.warning("Are you sure you want to delete this note?")
                c1, c2 = st.columns(2)
                with c1:
                    if st.button("Confirm Delete", type="primary"):
                        delete_note(note_id)
                        st.session_state.page = "list"
                        del st.session_state.delete_confirm
                        st.rerun()
                with c2:
                    if st.button("Cancel"):
                        st.session_state.delete_confirm = False
                        st.rerun()
    
    if st.button("Back to List"):
        st.session_state.page = "list"
        if "delete_confirm" in st.session_state:
            del st.session_state.delete_confirm
        st.rerun()


def notes_list_screen():
    st.header(f"QuickNotes for {st.session_state.username}")

    c1, c2, c3 = st.columns([1,1,1])
    with c1:
        if st.button("Create New Note"):
            st.session_state.page = "edit"
            st.session_state.current_note_id = None
            st.session_state.current_note = None
            st.rerun()
    
    with c2:
        if st.button("Support"):
            st.session_state.page = "support"
            st.rerun()
    
    with c3:
        if st.button("Logout"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    st.subheader("Your Notes")
    notes = get_notes()

    if not notes:
        st.info("You don't have any notes yet. Create one!")
    else:
        for note in notes:
            if st.button(note["title"], key=f"note_{note['id']}"):
                st.session_state.page = "edit"
                st.session_state.current_note_id = note["id"]
                st.session_state.current_note = note
                st.rerun()


# --- Main App Logic ---
def main():
    st.title("QuickNotes Application")

    # Initialize session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
    # If user is not logged in, show login page
    if not st.session_state.logged_in:
        login_page()
    else:
        # If user is logged in, show the main app
        if "page" not in st.session_state:
            st.session_state.page = "list"

        if st.session_state.page == "list":
            notes_list_screen()
        elif st.session_state.page == "edit":
            note_editor_screen()
        elif st.session_state.page == "support":
            support_page()

if __name__ == "__main__":
    main() 