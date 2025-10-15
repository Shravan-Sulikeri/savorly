from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.config import get_settings
from src.db.session import create_db_and_tables 

settings = get_settings()
app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")             
def on_startup():
    create_db_and_tables() 

@app.get("/health")
def health():
    return {"status": "ok", "service": "savorly-backend"}
from src.routers import recipes
app.include_router(recipes.router)
