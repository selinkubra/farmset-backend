# app/routers/farms.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import NodeFarm
from app.schemas import FarmCreate, FarmRead

router = APIRouter(prefix="/farms", tags=["Farms"])


@router.post("/", response_model=FarmRead, status_code=status.HTTP_201_CREATED)
def create_farm(farm_data: FarmCreate, session: Session = Depends(get_session)):
    """Yeni bir çiftlik kaydı oluşturur."""
    db_farm = NodeFarm.model_validate(farm_data)
    session.add(db_farm)
    session.commit()
    session.refresh(db_farm)
    return db_farm


@router.get("/", response_model=List[FarmRead])
def get_farms(session: Session = Depends(get_session)):
    """Kayıtlı tüm çiftlikleri listeler."""
    farms = session.exec(select(NodeFarm)).all()
    return farms


@router.get("/{farm_id}", response_model=FarmRead)
def get_farm(farm_id: int, session: Session = Depends(get_session)):
    """ID parametresine göre tek bir çiftlik detayını getirir."""
    farm = session.get(NodeFarm, farm_id)
    if not farm:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Çiftlik bulunamadı"
        )
    return farm