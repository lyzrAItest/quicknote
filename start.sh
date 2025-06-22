#!/bin/bash

# This script provides a convenient way to start both the backend and frontend applications.
# Before running, make sure you have installed all dependencies for both services
# as described in the README.md file.

# Function to handle cleanup of background processes when the script exits
cleanup() {
    echo "Shutting down the application..."
    # Kill the backend server process
    if [ -n "$BACKEND_PID" ]; then
        kill $BACKEND_PID
        echo "Backend server stopped."
    fi
    exit
}

# Trap the script's exit (e.g., via Ctrl+C) to call the cleanup function
trap cleanup SIGINT SIGTERM EXIT

# Navigate to the backend directory and start the FastAPI server in the background
echo "Starting backend server on http://127.0.0.1:8000..."
(cd backend && uvicorn main:app --host 0.0.0.0 --port 8000) &
BACKEND_PID=$!

# Give the backend a moment to initialize
sleep 3

# Navigate to the frontend directory and start the Streamlit app in the foreground
echo "Starting frontend application on http://localhost:8501..."
(cd frontend && streamlit run app.py)

# The 'trap' command will ensure the cleanup function is called when the script ends. 