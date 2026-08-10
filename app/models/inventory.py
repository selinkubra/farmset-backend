from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .farm import NodeFarm
    from .farm_set import NodeFarmSet


# =========================================================
# VEHICLE TYPE
# =========================================================

class NodeVehicleTypeBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    vehicle_type_name: Optional[str] = None
    vehicle_type_desc: Optional[str] = None
    vehicle_type_code: Optional[str] = None

    display_order: Optional[int] = None


class NodeVehicleType(NodeVehicleTypeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    vehicles: List["NodeVehicle"] = Relationship(
        back_populates="vehicle_type"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="vehicle_types"
    )


# =========================================================
# VEHICLE
# =========================================================

class NodeVehicleBase(SQLModel):
    farm_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarm.id"
    )

    vehicle_type_id: Optional[int] = Field(
        default=None,
        foreign_key="nodevehicletype.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    vehicle_name: Optional[str] = None
    vehicle_desc: Optional[str] = None

    plate_number: Optional[str] = None

    brand_name: Optional[str] = None
    model_name: Optional[str] = None
    model_year: Optional[int] = None

    serial_number: Optional[str] = None
    engine_number: Optional[str] = None
    chassis_number: Optional[str] = None

    purchase_date: Optional[datetime] = None
    sale_date: Optional[datetime] = None

    purchase_price: Optional[float] = None
    sale_price: Optional[float] = None
    current_value: Optional[float] = None

    display_order: Optional[int] = None


class NodeVehicle(NodeVehicleBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    farm: Optional["NodeFarm"] = Relationship()

    vehicle_type: Optional["NodeVehicleType"] = Relationship(
        back_populates="vehicles"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="vehicles"
    )


# =========================================================
# TOOL TYPE
# =========================================================

class NodeToolTypeBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    tool_type_name: Optional[str] = None
    tool_type_desc: Optional[str] = None
    tool_type_code: Optional[str] = None

    display_order: Optional[int] = None


class NodeToolType(NodeToolTypeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    tools: List["NodeTool"] = Relationship(
        back_populates="tool_type"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="tool_types"
    )


# =========================================================
# TOOL
# =========================================================

class NodeToolBase(SQLModel):
    farm_id: Optional[int] = None

    tool_type_id: Optional[int] = Field(
        default=None,
        foreign_key="nodetooltype.id"
    )

    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    tool_name: Optional[str] = None
    tool_desc: Optional[str] = None

    brand_name: Optional[str] = None
    model_name: Optional[str] = None
    serial_number: Optional[str] = None

    purchase_date: Optional[datetime] = None
    sale_date: Optional[datetime] = None

    purchase_price: Optional[float] = None
    sale_price: Optional[float] = None
    current_value: Optional[float] = None

    display_order: Optional[int] = None


class NodeTool(NodeToolBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    tool_type: Optional["NodeToolType"] = Relationship(
        back_populates="tools"
    )


# =========================================================
# SUPPLY TYPE
# =========================================================

class NodeSupplyTypeBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    supply_type_name: Optional[str] = None
    supply_type_desc: Optional[str] = None
    supply_type_code: Optional[str] = None

    unit_name: Optional[str] = None

    display_order: Optional[int] = None


class NodeSupplyType(NodeSupplyTypeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    supplies: List["NodeSupply"] = Relationship(
        back_populates="supply_type"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="supply_types"
    )


# =========================================================
# SUPPLY
# =========================================================

class NodeSupplyBase(SQLModel):
    farm_id: Optional[int] = None

    supply_type_id: Optional[int] = Field(
        default=None,
        foreign_key="nodesupplytype.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    supply_name: Optional[str] = None
    supply_desc: Optional[str] = None

    quantity: Optional[float] = None
    unit_price: Optional[float] = None
    total_value: Optional[float] = None

    purchase_date: Optional[datetime] = None
    expiration_date: Optional[datetime] = None

    display_order: Optional[int] = None


class NodeSupply(NodeSupplyBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    supply_type: Optional["NodeSupplyType"] = Relationship(
        back_populates="supplies"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="supplies"
    )