from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import NodeLand
from app.schemas import LandCreate, LandRead, LandUpdate


router = APIRouter(
    prefix="/lands",
    tags=["Lands"],
)


# =========================================================
# CREATE
# =========================================================

@router.post(
    "/",
    response_model=LandRead,
    status_code=status.HTTP_201_CREATED,
)
def create_land(
    land_data: LandCreate,
    session: Session = Depends(get_session),
):
    db_land = NodeLand.model_validate(land_data)

    session.add(db_land)
    session.commit()
    session.refresh(db_land)

    return db_land


# =========================================================
# READ ALL
# =========================================================

@router.get(
    "/",
    response_model=List[LandRead],
)
def get_lands(
    session: Session = Depends(get_session),
):
    lands = session.exec(
        select(NodeLand)
    ).all()

    return lands


# =========================================================
# READ ONE
# =========================================================

@router.get(
    "/{land_id}",
    response_model=LandRead,
)
def get_land(
    land_id: int,
    session: Session = Depends(get_session),
):
    land = session.get(NodeLand, land_id)

    if land is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Arazi bulunamadı",
        )

    return land


# =========================================================
# UPDATE
# =========================================================

@router.patch(
    "/{land_id}",
    response_model=LandRead,
)
def update_land(
    land_id: int,
    land_data: LandUpdate,
    session: Session = Depends(get_session),
):
    db_land = session.get(NodeLand, land_id)

    if db_land is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Arazi bulunamadı",
        )

    update_data = land_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(db_land, field, value)

    db_land.modification_date = datetime.utcnow()

    session.add(db_land)
    session.commit()
    session.refresh(db_land)

    return db_land


# =========================================================
# DELETE
# =========================================================

@router.delete(
    "/{land_id}",
    status_code=status.HTTP_200_OK,
)
def delete_land(
    land_id: int,
    session: Session = Depends(get_session),
):
    db_land = session.get(NodeLand, land_id)

    if db_land is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Arazi bulunamadı",
        )

    session.delete(db_land)
    session.commit()

    return {
        "message": "Arazi başarıyla silindi",
        "id": land_id,
    }