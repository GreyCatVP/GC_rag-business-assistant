#!/bin/bash
set -e
echo "🛠️  Activating venv..."
source venv/bin/activate
echo "🔐 Loading .env..."
export $(cat .env | xargs)
echo "🚀 Starting FastAPI + Streamlit..."
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000 &
python -m src.admin.admin
