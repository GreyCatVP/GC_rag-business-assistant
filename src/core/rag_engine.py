from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
import uuid

FAISS_PATH = Path("faiss_index")
KB_PATH = Path("knowledge")

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def add_file_to_index(file):
    text = file.read().decode("utf-8", errors="ignore")
    chunks = [Document(page_content=text, metadata={"source": file.filename})]
    if FAISS_PATH.exists():
        db = FAISS.load_local(str(FAISS_PATH), embeddings, allow_dangerous_deserialization=True)
    else:
        db = FAISS.from_documents([], embeddings)
    db.add_documents(chunks)
    db.save_local(str(FAISS_PATH))
    return len(chunks)

def search_docs(query: str, k: int = 3):
    if not FAISS_PATH.exists():
        return []
    db = FAISS.load_local(str(FAISS_PATH), embeddings, allow_dangerous_deserialization=True)
    docs = db.similarity_search(query, k=k)
    return [{"text": d.page_content, "source": d.metadata["source"]} for d in docs]

def get_catalog() -> str:
    """Возвращает JSON-каталог товаров (заглушка)"""
    from pathlib import Path
    import json
    catalog_path = Path("shop_data/catalog.json")
    if not catalog_path.exists():
        return "Каталог пуст."
    with catalog_path.open(encoding="utf-8") as f:
        items = json.load(f)
    return "\n".join(f"{i['name']} — {i['price']}₽" for i in items)

def get_logs(limit: int = 50) -> list[str]:
    """Возвращает последние N строк логов"""
    from pathlib import Path
    log_path = Path("logs/rag.log")
    if not log_path.exists():
        return ["Логов пока нет."]
    lines = log_path.read_text(encoding="utf-8").strip().splitlines()
    return lines[-limit:]
