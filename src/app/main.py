from datetime import datetime
from fastapi import FastAPI

app = FastAPI(title="FastAPI CMMI Demo", version="0.1.0")

@app.get("/health")
def read_health():
    """
    Retorna estado de salud simple.
    """
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(timespec="seconds")
    }
