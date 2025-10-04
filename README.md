# Cogent Application

This project demonstrates how to set up and run a ChromaDB instance using Docker, and how to run the `cogent_app.py` Python application.

## Prerequisites

- Docker must be installed on your machine.
- Python should be installed (Python 3.x for macOS).

## Setting Up ChromaDB

### Step 1: Install the necessary libraries required for this project

# Windows:
pip install -r requirements.txt

# Mac:
pip3 install -r requirements.txt

### Step 2: Start App and ChromaDB Using Docker Compose

# Windows:
docker-compose up --build

# Mac:
docker compose up --build

### Step 3: Verify the Container is Running

# Windows:
docker-compose ps

# Mac:
docker compose ps

### Step 4: Running the Python Application
Run below url in browser
    http://127.0.0.1:5000

### Step 5: To Stop the Container
Press CTRL+C to quit