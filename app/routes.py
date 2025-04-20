from fastapi import APIRouter
from .config import APP_NAME

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok", "app": APP_NAME}


@router.post("/echo")
def echo(data: dict):
    return {"you_sent": data}
