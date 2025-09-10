from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from api.upload import router as upload_router
from api.search import router as search_router
from api.webhook import router as webhook_router
from api.auth import router as auth_router
from admin.admin import admin_app

app = FastAPI(title="RAG Business Assistant", version="1.0.0")

# JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Роутеры
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(upload_router, prefix="/upload", tags=["upload"])
app.include_router(search_router, prefix="/search", tags=["search"])
app.include_router(webhook_router, prefix="/send", tags=["send"])

# Админ-страница
app.mount("/admin", admin_app)

@app.get("/")
def root():
    return {"message": "RAG Business Assistant API"}
