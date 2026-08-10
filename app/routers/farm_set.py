from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import NodeFarmSet


router = APIRouter(
    prefix="/farm-sets",
    tags=["Farm Sets"],
)


# =========================================================
# CREATE
# =========================================================

@router.post(
    "/",
    response_model=NodeFarmSet,
    status_code=status.HTTP_201_CREATED,
)
def create_farm_set(
    data: NodeFarmSet,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


# =========================================================
# READ ALL
# =========================================================

@router.get(
    "/",
    response_model=List[NodeFarmSet],
)
def read_farm_sets(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeFarmSet)
        .offset(skip)
        .limit(limit)
    ).all()


# =========================================================
# READ ONE
# =========================================================

@router.get(
    "/{farm_set_id}",
    response_model=NodeFarmSet,
)
def read_farm_set(
    farm_set_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeFarmSet, farm_set_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Farm set bulunamadı",
        )

    return db_item


# =========================================================
# UPDATE
# =========================================================

@router.patch(
    "/{farm_set_id}",
    response_model=NodeFarmSet,
)
def update_farm_set(
    farm_set_id: int,
    data: NodeFarmSet,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeFarmSet, farm_set_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Farm set bulunamadı",
        )

    update_data = data.model_dump(
        exclude_unset=True,
        exclude={
            "id",
            "creation_date",
            "modification_date",
        },
    )

    for field, value in update_data.items():
        setattr(db_item, field, value)

    db_item.modification_date = datetime.utcnow()

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


# =========================================================
# DELETE
# =========================================================

@router.delete(
    "/{farm_set_id}",
    status_code=status.HTTP_200_OK,
)
def delete_farm_set(
    farm_set_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeFarmSet, farm_set_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Farm set bulunamadı",
        )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Farm set başarıyla silindi",
        "id": farm_set_id,
    }