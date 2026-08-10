from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import NodeFarmer
from app.schemas import FarmerCreate, FarmerRead, FarmerUpdate


router = APIRouter(
    prefix="/farmers",
    tags=["Farmers"],
)


# =========================================================
# CREATE
# =========================================================

@router.post(
    "/",
    response_model=FarmerRead,
    status_code=status.HTTP_201_CREATED,
)
def create_farmer(
    farmer_data: FarmerCreate,
    session: Session = Depends(get_session),
):
    db_farmer = NodeFarmer.model_validate(farmer_data)

    session.add(db_farmer)
    session.commit()
    session.refresh(db_farmer)

    return db_farmer


# =========================================================
# READ ALL
# =========================================================

@router.get(
    "/",
    response_model=List[FarmerRead],
)
def get_farmers(
    session: Session = Depends(get_session),
):
    farmers = session.exec(
        select(NodeFarmer)
    ).all()

    return farmers


# =========================================================
# READ ONE
# =========================================================

@router.get(
    "/{farmer_id}",
    response_model=FarmerRead,
)
def get_farmer(
    farmer_id: int,
    session: Session = Depends(get_session),
):
    farmer = session.get(NodeFarmer, farmer_id)

    if farmer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Çiftçi bulunamadı",
        )

    return farmer


# =========================================================
# UPDATE
# =========================================================

@router.patch(
    "/{farmer_id}",
    response_model=FarmerRead,
)
def update_farmer(
    farmer_id: int,
    farmer_data: FarmerUpdate,
    session: Session = Depends(get_session),
):
    db_farmer = session.get(NodeFarmer, farmer_id)

    if db_farmer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Çiftçi bulunamadı",
        )

    update_data = farmer_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(db_farmer, field, value)

    db_farmer.modification_date = datetime.utcnow()

    session.add(db_farmer)
    session.commit()
    session.refresh(db_farmer)

    return db_farmer


# =========================================================
# DELETE
# =========================================================

@router.delete(
    "/{farmer_id}",
    status_code=status.HTTP_200_OK,
)
def delete_farmer(
    farmer_id: int,
    session: Session = Depends(get_session),
):
    db_farmer = session.get(NodeFarmer, farmer_id)

    if db_farmer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Çiftçi bulunamadı",
        )

    session.delete(db_farmer)
    session.commit()

    return {
        "message": "Çiftçi başarıyla silindi",
        "id": farmer_id,
    }