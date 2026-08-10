from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import NodeFarm
from app.schemas import FarmCreate, FarmRead, FarmUpdate


router = APIRouter(
    prefix="/farms",
    tags=["Farms"],
)


# =========================================================
# CREATE
# =========================================================

@router.post(
    "/",
    response_model=FarmRead,
    status_code=status.HTTP_201_CREATED,
)
def create_farm(
    farm_data: FarmCreate,
    session: Session = Depends(get_session),
):
    db_farm = NodeFarm.model_validate(farm_data)

    session.add(db_farm)
    session.commit()
    session.refresh(db_farm)

    return db_farm


# =========================================================
# READ ALL
# =========================================================

@router.get(
    "/",
    response_model=List[FarmRead],
)
def get_farms(
    session: Session = Depends(get_session),
):
    farms = session.exec(
        select(NodeFarm)
    ).all()

    return farms


# =========================================================
# READ ONE
# =========================================================

@router.get(
    "/{farm_id}",
    response_model=FarmRead,
)
def get_farm(
    farm_id: int,
    session: Session = Depends(get_session),
):
    farm = session.get(NodeFarm, farm_id)

    if farm is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Çiftlik bulunamadı",
        )

    return farm


# =========================================================
# UPDATE
# =========================================================

@router.patch(
    "/{farm_id}",
    response_model=FarmRead,
)
def update_farm(
    farm_id: int,
    farm_data: FarmUpdate,
    session: Session = Depends(get_session),
):
    db_farm = session.get(NodeFarm, farm_id)

    if db_farm is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Çiftlik bulunamadı",
        )

    update_data = farm_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(db_farm, field, value)

    db_farm.modification_date = datetime.utcnow()

    session.add(db_farm)
    session.commit()
    session.refresh(db_farm)

    return db_farm


# =========================================================
# DELETE
# =========================================================

@router.delete(
    "/{farm_id}",
    status_code=status.HTTP_200_OK,
)
def delete_farm(
    farm_id: int,
    session: Session = Depends(get_session),
):
    db_farm = session.get(NodeFarm, farm_id)

    if db_farm is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Çiftlik bulunamadı",
        )

    session.delete(db_farm)
    session.commit()

    return {
        "message": "Çiftlik başarıyla silindi",
        "id": farm_id,
    }