from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/health", tags=["Health Check"])


@router.get("/", summary="Basic health check")
def health_check():
    """Returns API status — use this to ping the server."""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "Hello Health API",
    }


@router.get("/ping", summary="Simple ping")
def ping():
    """Lightest possible check — just returns pong."""
    return {"ping": "pong"}
