from fastapi import FastAPI
from src.database import create_db
from src.controllers import todo_controller

app = FastAPI()

@app.on_event("startup")
async def startup() -> None:
    create_db()

app.include_router(todo_controller, prefix="/todo")