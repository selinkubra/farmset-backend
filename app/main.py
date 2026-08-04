# app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database import create_db_and_tables
from app.routers import farms


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Uygulama başlarken veritabanını ve tüm tabloları otomatik oluşturur
    create_db_and_tables()
    yield


app = FastAPI(
    title="Çiftlik Yönetim Sistemi API",
    version="1.0.0",
    lifespan=lifespan,
)

# Router'ları ana uygulamaya ekleme
app.include_router(farms.router)


@app.get("/")
def read_root():
    return {"message": "Çiftlik Yönetim Sistemi API Hazır!"}