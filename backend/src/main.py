from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from dotenv import load_dotenv
import os
from src.database import create_db, SessionLocal
from src.middlewares import AuthenticationMiddleware
from src.controllers import todo_controller
from src.controllers import user_controller

app = FastAPI()

load_dotenv()

@app.on_event('startup')
async def startup() -> None:
    create_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv('FRONTEND_URL')],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(AuthenticationMiddleware)

app.include_router(todo_controller, prefix='/todo')
app.include_router(user_controller, prefix='/user')

@app.get("/")
async def health_check():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()

        return JSONResponse(
            content={"status": "ok"},
            status_code=status.HTTP_200_OK
        )
    except Exception as e:
        return JSONResponse(
            content={"status": "fail", "error": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )