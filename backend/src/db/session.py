from sqlmodel import SQLModel, create_engine, Session
from src.core.config import get_settings

settings = get_settings()

# Ensure we use a sync SQLite URL (not aiosqlite) for simplicity
db_url = settings.DATABASE_URL.replace("sqlite+aiosqlite", "sqlite")

engine = create_engine(db_url, echo=False)

def get_session() -> Session:
    return Session(engine)

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)
