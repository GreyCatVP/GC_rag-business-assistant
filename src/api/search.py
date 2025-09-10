from fastapi import APIRouter, Depends, Query
from fastapi.security import OAuth2PasswordBearer
from core.rag_engine import search_docs

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/")
def search(query: str = Query(...), k: int = Query(3), token: str = Depends(oauth2_scheme)):
    results = search_docs(query, k)
    return {"results": results}
