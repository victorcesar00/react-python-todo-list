import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autoflush=False, bind=engine)


def create_db() -> None:
    Base.metadata.create_all(bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
