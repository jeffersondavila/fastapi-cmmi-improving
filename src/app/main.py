from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI(title="FastAPI CMMI Demo", version="0.1.0")

@app.get("/health")
def read_health():
    """
    Retorna estado de salud simple.
    """
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds")
    }
