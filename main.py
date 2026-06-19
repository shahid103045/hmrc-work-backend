from fastapi import FastAPI
import os

app = FastAPI(title="HMRC Emergency AI Backend", version="1.0")

@app.get("/")
def home():
    return {"status": "Backend live Sir ✅", "repo": "hmrc-work-backend", "message": "Ready for HMRC + Emergency AI"}

@app.get("/health")
def health():
    return {"ok": True, "service": "running"}

@app.post("/emergency/process")
def emergency(data: dict):
    return {"received": data, "action": "AI will process here", "status": "success"}
