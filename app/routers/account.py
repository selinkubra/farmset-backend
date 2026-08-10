from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import NodeAccount


router = APIRouter(
    prefix="/accounts",
    tags=["Accounts (Hesaplar)"],
)


# =========================================================
# CREATE
# =========================================================

@router.post(
    "/",
    response_model=NodeAccount,
    status_code=status.HTTP_201_CREATED,
)
def create_account(
    data: NodeAccount,
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
    response_model=List[NodeAccount],
)
def read_accounts(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeAccount)
        .offset(skip)
        .limit(limit)
    ).all()


# =========================================================
# READ ONE
# =========================================================

@router.get(
    "/{account_id}",
    response_model=NodeAccount,
)
def read_account(
    account_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeAccount, account_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hesap bulunamadı",
        )

    return db_item


# =========================================================
# UPDATE
# =========================================================

@router.patch(
    "/{account_id}",
    response_model=NodeAccount,
)
def update_account(
    account_id: int,
    data: NodeAccount,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeAccount, account_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hesap bulunamadı",
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
    "/{account_id}",
    status_code=status.HTTP_200_OK,
)
def delete_account(
    account_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeAccount, account_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hesap bulunamadı",
        )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Hesap başarıyla silindi",
        "id": account_id,
    }