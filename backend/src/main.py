from fastapi import FastAPI
from src.database import create_db

app = FastAPI()

@app.on_event("startup")
async def startup():
    create_db()