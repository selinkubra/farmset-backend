from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from app.database import get_session
from app.models.inventory import NodeVehicleType

router = APIRouter(prefix="/inventory", tags=["Inventory (Envanter)"])

@router.post("/vehicles/types/", response_model=NodeVehicleType)
def create_vehicle_type(vehicle_type: NodeVehicleType, session: Session = Depends(get_session)):
    session.add(vehicle_type)
    session.commit()
    session.refresh(vehicle_type)
    return vehicle_type

@router.get("/vehicles/types/", response_model=List[NodeVehicleType])
def read_vehicle_types(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    vehicle_types = session.exec(select(NodeVehicleType).offset(skip).limit(limit)).all()
    return vehicle_types
