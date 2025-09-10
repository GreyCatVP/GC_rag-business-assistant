from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.security import OAuth2PasswordBearer
from core.rag_engine import add_file_to_index
from typing import List

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/")
def upload_files(files: List[UploadFile] = File(...), token: str = Depends(oauth2_scheme)):
    total = 0
    for file in files:
        total += add_file_to_index(file)
    return {"message": f"Added {total} chunks"}
