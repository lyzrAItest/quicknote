# QuickNotes Application

This project is a simple, lightweight note-taking application with a FastAPI backend and a Streamlit frontend.

## Project Structure
```
.
├── backend
│   ├── main.py
│   └── requirements.txt
└── frontend
    ├── app.py
    └── requirements.txt
```

## How to Run the Application

You will need to run two separate processes in two different terminals: one for the backend and one for the frontend.

### 1. Run the Backend (FastAPI)

First, navigate to the backend directory and install the required packages.

```bash
# Go to the backend directory
cd backend

# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload
```
The backend server will start on `http://127.0.0.1:8000`.

### 2. Run the Frontend (Streamlit)

Open a **new terminal** window. Navigate to the frontend directory and install its dependencies.

```bash
# Go to the frontend directory from the root
cd frontend

# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```
The frontend application will open in your web browser, usually at `http://localhost:8501`.

You can now use the QuickNotes application! 