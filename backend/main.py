from fastapi import FastAPI
from backend.websocket import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def health():
    return {"status": "2CareAI Voice Agent Running"}