from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import NodeFarmDoc, NodeFarmMedia


router = APIRouter(
    prefix="/media",
    tags=["Media (Doküman ve Medya)"],
)


# =========================================================
# FARM DOC CRUD
# =========================================================

@router.post(
    "/docs/",
    response_model=NodeFarmDoc,
    status_code=status.HTTP_201_CREATED,
)
def create_farm_doc(
    data: NodeFarmDoc,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/docs/",
    response_model=List[NodeFarmDoc],
)
def read_farm_docs(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeFarmDoc)
        .offset(skip)
        .limit(limit)
    ).all()


@router.get(
    "/docs/{doc_id}",
    response_model=NodeFarmDoc,
)
def read_farm_doc(
    doc_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeFarmDoc, doc_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Doküman kaydı bulunamadı",
        )

    return db_item


@router.patch(
    "/docs/{doc_id}",
    response_model=NodeFarmDoc,
)
def update_farm_doc(
    doc_id: int,
    data: NodeFarmDoc,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeFarmDoc, doc_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Doküman kaydı bulunamadı",
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


@router.delete(
    "/docs/{doc_id}",
    status_code=status.HTTP_200_OK,
)
def delete_farm_doc(
    doc_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeFarmDoc, doc_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Doküman kaydı bulunamadı",
        )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Doküman kaydı başarıyla silindi",
        "id": doc_id,
    }


# =========================================================
# FARM MEDIA CRUD
# =========================================================

@router.post(
    "/farm-media/",
    response_model=NodeFarmMedia,
    status_code=status.HTTP_201_CREATED,
)
def create_farm_media(
    data: NodeFarmMedia,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/farm-media/",
    response_model=List[NodeFarmMedia],
)
def read_farm_media_list(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeFarmMedia)
        .offset(skip)
        .limit(limit)
    ).all()


@router.get(
    "/farm-media/{media_record_id}",
    response_model=NodeFarmMedia,
)
def read_farm_media(
    media_record_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeFarmMedia, media_record_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Medya kaydı bulunamadı",
        )

    return db_item


@router.patch(
    "/farm-media/{media_record_id}",
    response_model=NodeFarmMedia,
)
def update_farm_media(
    media_record_id: int,
    data: NodeFarmMedia,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeFarmMedia, media_record_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Medya kaydı bulunamadı",
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


@router.delete(
    "/farm-media/{media_record_id}",
    status_code=status.HTTP_200_OK,
)
def delete_farm_media(
    media_record_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeFarmMedia, media_record_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Medya kaydı bulunamadı",
        )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Medya kaydı başarıyla silindi",
        "id": media_record_id,
    }