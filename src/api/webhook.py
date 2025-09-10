from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
import httpx, os

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/")
def send_to_crm(data: dict, token: str = Depends(oauth2_scheme)):
    # Пример: отправка в Bitrix24
    bitrix_webhook = os.getenv("BITRIX_WEBHOOK_URL")
    if bitrix_webhook:
        payload = {"fields": {"TITLE": data["title"], "DESCRIPTION": data["description"]}}
        httpx.post(bitrix_webhook, json=payload)
    return {"message": "Sent to CRM"}
