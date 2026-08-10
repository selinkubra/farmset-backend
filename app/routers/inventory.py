from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import (
    NodeVehicle,
    NodeVehicleType,
    NodeTool,
    NodeToolType,
    NodeSupply,
    NodeSupplyType,
)
from app.schemas import (
    VehicleCreate,
    VehicleRead,
    VehicleUpdate,
    VehicleTypeCreate,
    VehicleTypeRead,
    VehicleTypeUpdate,
    ToolCreate,
    ToolRead,
    ToolUpdate,
    ToolTypeCreate,
    ToolTypeRead,
    ToolTypeUpdate,
    SupplyCreate,
    SupplyRead,
    SupplyUpdate,
    SupplyTypeCreate,
    SupplyTypeRead,
    SupplyTypeUpdate,
)


router = APIRouter(
    prefix="/inventory",
    tags=["Inventory (Envanter)"],
)


# =========================================================
# VEHICLE TYPE CRUD
# =========================================================

@router.post(
    "/vehicles/types/",
    response_model=VehicleTypeRead,
    status_code=status.HTTP_201_CREATED,
)
def create_vehicle_type(
    data: VehicleTypeCreate,
    session: Session = Depends(get_session),
):
    db_item = NodeVehicleType.model_validate(data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.get(
    "/vehicles/types/",
    response_model=List[VehicleTypeRead],
)
def read_vehicle_types(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeVehicleType)
        .offset(skip)
        .limit(limit)
    ).all()


@router.get(
    "/vehicles/types/{vehicle_type_id}",
    response_model=VehicleTypeRead,
)
def read_vehicle_type(
    vehicle_type_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeVehicleType, vehicle_type_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Araç tipi bulunamadı",
        )

    return db_item


@router.patch(
    "/vehicles/types/{vehicle_type_id}",
    response_model=VehicleTypeRead,
)
def update_vehicle_type(
    vehicle_type_id: int,
    data: VehicleTypeUpdate,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeVehicleType, vehicle_type_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Araç tipi bulunamadı",
        )

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(db_item, field, value)

    db_item.modification_date = datetime.utcnow()

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/vehicles/types/{vehicle_type_id}",
    status_code=status.HTTP_200_OK,
)
def delete_vehicle_type(
    vehicle_type_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeVehicleType, vehicle_type_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Araç tipi bulunamadı",
        )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Araç tipi başarıyla silindi",
        "id": vehicle_type_id,
    }


# =========================================================
# VEHICLE CRUD
# =========================================================

@router.post(
    "/vehicles/",
    response_model=VehicleRead,
    status_code=status.HTTP_201_CREATED,
)
def create_vehicle(
    data: VehicleCreate,
    session: Session = Depends(get_session),
):
    db_item = NodeVehicle.model_validate(data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.get(
    "/vehicles/",
    response_model=List[VehicleRead],
)
def read_vehicles(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeVehicle)
        .offset(skip)
        .limit(limit)
    ).all()


@router.get(
    "/vehicles/{vehicle_id}",
    response_model=VehicleRead,
)
def read_vehicle(
    vehicle_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeVehicle, vehicle_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Araç bulunamadı",
        )

    return db_item


@router.patch(
    "/vehicles/{vehicle_id}",
    response_model=VehicleRead,
)
def update_vehicle(
    vehicle_id: int,
    data: VehicleUpdate,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeVehicle, vehicle_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Araç bulunamadı",
        )

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(db_item, field, value)

    db_item.modification_date = datetime.utcnow()

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/vehicles/{vehicle_id}",
    status_code=status.HTTP_200_OK,
)
def delete_vehicle(
    vehicle_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeVehicle, vehicle_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Araç bulunamadı",
        )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Araç başarıyla silindi",
        "id": vehicle_id,
    }


# =========================================================
# TOOL TYPE CRUD
# =========================================================

@router.post(
    "/tools/types/",
    response_model=ToolTypeRead,
    status_code=status.HTTP_201_CREATED,
)
def create_tool_type(
    data: ToolTypeCreate,
    session: Session = Depends(get_session),
):
    db_item = NodeToolType.model_validate(data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.get(
    "/tools/types/",
    response_model=List[ToolTypeRead],
)
def read_tool_types(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeToolType)
    ).all()


@router.get(
    "/tools/types/{tool_type_id}",
    response_model=ToolTypeRead,
)
def read_tool_type(
    tool_type_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeToolType, tool_type_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ekipman tipi bulunamadı",
        )

    return db_item


@router.patch(
    "/tools/types/{tool_type_id}",
    response_model=ToolTypeRead,
)
def update_tool_type(
    tool_type_id: int,
    data: ToolTypeUpdate,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeToolType, tool_type_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ekipman tipi bulunamadı",
        )

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(db_item, field, value)

    db_item.modification_date = datetime.utcnow()

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/tools/types/{tool_type_id}",
    status_code=status.HTTP_200_OK,
)
def delete_tool_type(
    tool_type_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeToolType, tool_type_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ekipman tipi bulunamadı",
        )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Ekipman tipi başarıyla silindi",
        "id": tool_type_id,
    }


# =========================================================
# TOOL CRUD
# =========================================================

@router.post(
    "/tools/",
    response_model=ToolRead,
    status_code=status.HTTP_201_CREATED,
)
def create_tool(
    data: ToolCreate,
    session: Session = Depends(get_session),
):
    db_item = NodeTool.model_validate(data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.get(
    "/tools/",
    response_model=List[ToolRead],
)
def read_tools(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeTool)
    ).all()


@router.get(
    "/tools/{tool_id}",
    response_model=ToolRead,
)
def read_tool(
    tool_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeTool, tool_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ekipman bulunamadı",
        )

    return db_item


@router.patch(
    "/tools/{tool_id}",
    response_model=ToolRead,
)
def update_tool(
    tool_id: int,
    data: ToolUpdate,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeTool, tool_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ekipman bulunamadı",
        )

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(db_item, field, value)

    db_item.modification_date = datetime.utcnow()

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/tools/{tool_id}",
    status_code=status.HTTP_200_OK,
)
def delete_tool(
    tool_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeTool, tool_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ekipman bulunamadı",
        )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Ekipman başarıyla silindi",
        "id": tool_id,
    }


# =========================================================
# SUPPLY TYPE CRUD
# =========================================================

@router.post(
    "/supplies/types/",
    response_model=SupplyTypeRead,
    status_code=status.HTTP_201_CREATED,
)
def create_supply_type(
    data: SupplyTypeCreate,
    session: Session = Depends(get_session),
):
    db_item = NodeSupplyType.model_validate(data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.get(
    "/supplies/types/",
    response_model=List[SupplyTypeRead],
)
def read_supply_types(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeSupplyType)
    ).all()


@router.get(
    "/supplies/types/{supply_type_id}",
    response_model=SupplyTypeRead,
)
def read_supply_type(
    supply_type_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeSupplyType, supply_type_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Malzeme tipi bulunamadı",
        )

    return db_item


@router.patch(
    "/supplies/types/{supply_type_id}",
    response_model=SupplyTypeRead,
)
def update_supply_type(
    supply_type_id: int,
    data: SupplyTypeUpdate,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeSupplyType, supply_type_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Malzeme tipi bulunamadı",
        )

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(db_item, field, value)

    db_item.modification_date = datetime.utcnow()

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/supplies/types/{supply_type_id}",
    status_code=status.HTTP_200_OK,
)
def delete_supply_type(
    supply_type_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeSupplyType, supply_type_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Malzeme tipi bulunamadı",
        )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Malzeme tipi başarıyla silindi",
        "id": supply_type_id,
    }


# =========================================================
# SUPPLY CRUD
# =========================================================

@router.post(
    "/supplies/",
    response_model=SupplyRead,
    status_code=status.HTTP_201_CREATED,
)
def create_supply(
    data: SupplyCreate,
    session: Session = Depends(get_session),
):
    db_item = NodeSupply.model_validate(data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.get(
    "/supplies/",
    response_model=List[SupplyRead],
)
def read_supplies(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeSupply)
    ).all()


@router.get(
    "/supplies/{supply_id}",
    response_model=SupplyRead,
)
def read_supply(
    supply_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeSupply, supply_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Malzeme bulunamadı",
        )

    return db_item


@router.patch(
    "/supplies/{supply_id}",
    response_model=SupplyRead,
)
def update_supply(
    supply_id: int,
    data: SupplyUpdate,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeSupply, supply_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Malzeme bulunamadı",
        )

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(db_item, field, value)

    db_item.modification_date = datetime.utcnow()

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/supplies/{supply_id}",
    status_code=status.HTTP_200_OK,
)
def delete_supply(
    supply_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeSupply, supply_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Malzeme bulunamadı",
        )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Malzeme başarıyla silindi",
        "id": supply_id,
    }