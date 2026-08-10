from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import (
    NodePlant,
    NodePlantType,
    NodePlantTypeInfo,
    NodeTree,
)
from app.schemas import (
    PlantCreate,
    PlantRead,
    PlantUpdate,
    PlantTypeCreate,
    PlantTypeRead,
    PlantTypeUpdate,
    PlantTypeInfoCreate,
    PlantTypeInfoRead,
    PlantTypeInfoUpdate,
    TreeCreate,
    TreeRead,
    TreeUpdate,
)


router = APIRouter(
    prefix="/plants",
    tags=["Plants (Bitkiler)"],
)


# =========================================================
# PLANT TYPE CRUD
# =========================================================

@router.post(
    "/types/",
    response_model=PlantTypeRead,
    status_code=status.HTTP_201_CREATED,
)
def create_plant_type(
    plant_type_data: PlantTypeCreate,
    session: Session = Depends(get_session),
):
    db_plant_type = NodePlantType.model_validate(plant_type_data)

    session.add(db_plant_type)
    session.commit()
    session.refresh(db_plant_type)

    return db_plant_type


@router.get(
    "/types/",
    response_model=List[PlantTypeRead],
)
def read_plant_types(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodePlantType)
        .offset(skip)
        .limit(limit)
    ).all()


@router.get(
    "/types/{plant_type_id}",
    response_model=PlantTypeRead,
)
def read_plant_type(
    plant_type_id: int,
    session: Session = Depends(get_session),
):
    db_plant_type = session.get(NodePlantType, plant_type_id)

    if db_plant_type is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bitki tipi bulunamadı",
        )

    return db_plant_type


@router.patch(
    "/types/{plant_type_id}",
    response_model=PlantTypeRead,
)
def update_plant_type(
    plant_type_id: int,
    plant_type_data: PlantTypeUpdate,
    session: Session = Depends(get_session),
):
    db_plant_type = session.get(NodePlantType, plant_type_id)

    if db_plant_type is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bitki tipi bulunamadı",
        )

    for field, value in plant_type_data.model_dump(
        exclude_unset=True
    ).items():
        setattr(db_plant_type, field, value)

    db_plant_type.modification_date = datetime.utcnow()

    session.add(db_plant_type)
    session.commit()
    session.refresh(db_plant_type)

    return db_plant_type


@router.delete(
    "/types/{plant_type_id}",
    status_code=status.HTTP_200_OK,
)
def delete_plant_type(
    plant_type_id: int,
    session: Session = Depends(get_session),
):
    db_plant_type = session.get(NodePlantType, plant_type_id)

    if db_plant_type is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bitki tipi bulunamadı",
        )

    session.delete(db_plant_type)
    session.commit()

    return {
        "message": "Bitki tipi başarıyla silindi",
        "id": plant_type_id,
    }


# =========================================================
# PLANT CRUD
# =========================================================

@router.post(
    "/",
    response_model=PlantRead,
    status_code=status.HTTP_201_CREATED,
)
def create_plant(
    plant_data: PlantCreate,
    session: Session = Depends(get_session),
):
    db_plant = NodePlant.model_validate(plant_data)

    session.add(db_plant)
    session.commit()
    session.refresh(db_plant)

    return db_plant


@router.get(
    "/",
    response_model=List[PlantRead],
)
def read_plants(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodePlant)
        .offset(skip)
        .limit(limit)
    ).all()


@router.get(
    "/{plant_id}",
    response_model=PlantRead,
)
def read_plant(
    plant_id: int,
    session: Session = Depends(get_session),
):
    db_plant = session.get(NodePlant, plant_id)

    if db_plant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bitki bulunamadı",
        )

    return db_plant


@router.patch(
    "/{plant_id}",
    response_model=PlantRead,
)
def update_plant(
    plant_id: int,
    plant_data: PlantUpdate,
    session: Session = Depends(get_session),
):
    db_plant = session.get(NodePlant, plant_id)

    if db_plant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bitki bulunamadı",
        )

    for field, value in plant_data.model_dump(
        exclude_unset=True
    ).items():
        setattr(db_plant, field, value)

    db_plant.modification_date = datetime.utcnow()

    session.add(db_plant)
    session.commit()
    session.refresh(db_plant)

    return db_plant


@router.delete(
    "/{plant_id}",
    status_code=status.HTTP_200_OK,
)
def delete_plant(
    plant_id: int,
    session: Session = Depends(get_session),
):
    db_plant = session.get(NodePlant, plant_id)

    if db_plant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bitki bulunamadı",
        )

    session.delete(db_plant)
    session.commit()

    return {
        "message": "Bitki başarıyla silindi",
        "id": plant_id,
    }


# =========================================================
# PLANT TYPE INFO CRUD
# =========================================================

@router.post(
    "/type-infos/",
    response_model=PlantTypeInfoRead,
    status_code=status.HTTP_201_CREATED,
)
def create_plant_type_info(
    info_data: PlantTypeInfoCreate,
    session: Session = Depends(get_session),
):
    db_info = NodePlantTypeInfo.model_validate(info_data)

    session.add(db_info)
    session.commit()
    session.refresh(db_info)

    return db_info


@router.get(
    "/type-infos/",
    response_model=List[PlantTypeInfoRead],
)
def read_plant_type_infos(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodePlantTypeInfo)
    ).all()


@router.get(
    "/type-infos/{info_id}",
    response_model=PlantTypeInfoRead,
)
def read_plant_type_info(
    info_id: int,
    session: Session = Depends(get_session),
):
    db_info = session.get(NodePlantTypeInfo, info_id)

    if db_info is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bitki tipi bilgisi bulunamadı",
        )

    return db_info


@router.patch(
    "/type-infos/{info_id}",
    response_model=PlantTypeInfoRead,
)
def update_plant_type_info(
    info_id: int,
    info_data: PlantTypeInfoUpdate,
    session: Session = Depends(get_session),
):
    db_info = session.get(NodePlantTypeInfo, info_id)

    if db_info is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bitki tipi bilgisi bulunamadı",
        )

    for field, value in info_data.model_dump(
        exclude_unset=True
    ).items():
        setattr(db_info, field, value)

    db_info.modification_date = datetime.utcnow()

    session.add(db_info)
    session.commit()
    session.refresh(db_info)

    return db_info


@router.delete(
    "/type-infos/{info_id}",
    status_code=status.HTTP_200_OK,
)
def delete_plant_type_info(
    info_id: int,
    session: Session = Depends(get_session),
):
    db_info = session.get(NodePlantTypeInfo, info_id)

    if db_info is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bitki tipi bilgisi bulunamadı",
        )

    session.delete(db_info)
    session.commit()

    return {
        "message": "Bitki tipi bilgisi başarıyla silindi",
        "id": info_id,
    }


# =========================================================
# TREE CRUD
# =========================================================

@router.post(
    "/trees/",
    response_model=TreeRead,
    status_code=status.HTTP_201_CREATED,
)
def create_tree(
    tree_data: TreeCreate,
    session: Session = Depends(get_session),
):
    db_tree = NodeTree.model_validate(tree_data)

    session.add(db_tree)
    session.commit()
    session.refresh(db_tree)

    return db_tree


@router.get(
    "/trees/",
    response_model=List[TreeRead],
)
def read_trees(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeTree)
    ).all()


@router.get(
    "/trees/{tree_id}",
    response_model=TreeRead,
)
def read_tree(
    tree_id: int,
    session: Session = Depends(get_session),
):
    db_tree = session.get(NodeTree, tree_id)

    if db_tree is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ağaç bulunamadı",
        )

    return db_tree


@router.patch(
    "/trees/{tree_id}",
    response_model=TreeRead,
)
def update_tree(
    tree_id: int,
    tree_data: TreeUpdate,
    session: Session = Depends(get_session),
):
    db_tree = session.get(NodeTree, tree_id)

    if db_tree is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ağaç bulunamadı",
        )

    for field, value in tree_data.model_dump(
        exclude_unset=True
    ).items():
        setattr(db_tree, field, value)

    db_tree.modification_date = datetime.utcnow()

    session.add(db_tree)
    session.commit()
    session.refresh(db_tree)

    return db_tree


@router.delete(
    "/trees/{tree_id}",
    status_code=status.HTTP_200_OK,
)
def delete_tree(
    tree_id: int,
    session: Session = Depends(get_session),
):
    db_tree = session.get(NodeTree, tree_id)

    if db_tree is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ağaç bulunamadı",
        )

    session.delete(db_tree)
    session.commit()

    return {
        "message": "Ağaç başarıyla silindi",
        "id": tree_id,
    }