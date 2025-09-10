#!/bin/bash
set -e
echo "🛠️  Activating venv..."
source venv/bin/activate 2>/dev/null || { echo "❌ Activate venv first"; exit 1; }
echo "🔐 Loading .env..."
export $(cat .env | xargs)
echo "🚀 Starting FastAPI + Streamlit..."
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000 &
streamlit run src/admin/admin.py --server.port=8501 --server.address=0.0.0.0
