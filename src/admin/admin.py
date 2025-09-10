import streamlit as st
from core.rag_engine import get_catalog, get_logs

st.set_page_config(page_title="Admin Panel", layout="wide")
st.title("🔧 RAG Business Assistant — Admin")

with st.sidebar:
    st.subheader("Модули")
    avatar_on = st.toggle("Аватар бренда", True)
    shop_on = st.toggle("Магазин", True)
    rag_on = st.toggle("FAQ", True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("📁 Загрузка файлов")
    files = st.file_uploader("PDF/DOCX/TXT", type=["pdf", "docx", "txt"], accept_multiple_files=True)
    if files:
        with st.spinner("Обрабатываю..."):
            total = 0
            for f in files:
                total += add_file_to_index(f)
            st.success(f"Добавлено чанков: {total}")

with col2:
    st.subheader("📊 Логи")
    logs = get_logs(limit=50)
    for log in logs:
        st.code(log)
