from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import create_db_and_tables
from app.routers import (
    farms,
    lands,
    farmers,
    users,
    plants,
    inventory,
    environment,
    finance,
    account,
    farm_set,
    media,
    core_extra,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="Çiftlik Yönetim Sistemi API",
    version="1.0.0",
    lifespan=lifespan,
)


app.include_router(farms.router)
app.include_router(lands.router)
app.include_router(farmers.router)
app.include_router(users.router)
app.include_router(plants.router)
app.include_router(inventory.router)
app.include_router(environment.router)
app.include_router(finance.router)
app.include_router(account.router)
app.include_router(farm_set.router)
app.include_router(media.router)
app.include_router(core_extra.router)


@app.get("/")
def read_root():
    return {
        "message": "Çiftlik Yönetim Sistemi API Hazır!"
    }