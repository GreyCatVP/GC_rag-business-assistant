#!/bin/bash
set -e
echo "🛠️  Activating venv..."
source venv/bin/activate
echo "🔐 Loading .env..."
export $(cat .env | xargs)
echo "🚀 Starting FastAPI + Streamlit..."
python -m src.main &
python -m src.admin.admin
