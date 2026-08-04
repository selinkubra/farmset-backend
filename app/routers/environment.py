from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from app.database import get_session
from app.models.environment import NodeSeason, NodeSoilType

router = APIRouter(prefix="/environment", tags=["Environment (Çevre ve Sezon)"])

# Sezon İşlemleri
@router.post("/seasons/", response_model=NodeSeason)
def create_season(season: NodeSeason, session: Session = Depends(get_session)):
    session.add(season)
    session.commit()
    session.refresh(season)
    return season

@router.get("/seasons/", response_model=List[NodeSeason])
def read_seasons(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    seasons = session.exec(select(NodeSeason).offset(skip).limit(limit)).all()
    return seasons
