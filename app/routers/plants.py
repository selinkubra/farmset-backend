from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from app.database import get_session
from app.models.plant import NodePlantType

router = APIRouter(prefix="/plants", tags=["Plants (Bitkiler)"])

@router.post("/types/", response_model=NodePlantType)
def create_plant_type(plant_type: NodePlantType, session: Session = Depends(get_session)):
    session.add(plant_type)
    session.commit()
    session.refresh(plant_type)
    return plant_type

@router.get("/types/", response_model=List[NodePlantType])
def read_plant_types(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    plant_types = session.exec(select(NodePlantType).offset(skip).limit(limit)).all()
    return plant_types
