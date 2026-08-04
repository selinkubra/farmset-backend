from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

class NodeVehicleTypeBase(SQLModel):
    farm_set_id: Optional[int] = Field(default=None, index=True)
    vehicle_type_name: str = Field(index=True)
    vehicle_type_desc: Optional[str] = Field(default=None)
    display_order: Optional[int] = Field(default=0)

class NodeVehicleType(NodeVehicleTypeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) # Java'daki vehicleTypeId
    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)
class NodeVehicleBase(SQLModel):
    vehicle_type_id: Optional[int] = Field(default=None, index=True)
    farm_id: Optional[int] = Field(default=None, index=True)
    plate_number: Optional[str] = Field(default=None)
    status: Optional[str] = Field(default="ACTIVE")
class NodeVehicle(NodeVehicleBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: datetime = Field(default_factory=datetime.utcnow)
class NodeToolTypeBase(SQLModel):
    name: str = Field(index=True)
    description: Optional[str] = Field(default=None)
class NodeToolType(NodeToolTypeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: datetime = Field(default_factory=datetime.utcnow)
class NodeToolBase(SQLModel):
    tool_type_id: Optional[int] = Field(default=None, index=True)
    farm_id: Optional[int] = Field(default=None, index=True)
    serial_number: Optional[str] = Field(default=None)
class NodeTool(NodeToolBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: datetime = Field(default_factory=datetime.utcnow)
class NodeSupplyTypeBase(SQLModel):
    name: str = Field(index=True)
    unit: str # Örn: "KG", "Litre", "Adet"
class NodeSupplyType(NodeSupplyTypeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: datetime = Field(default_factory=datetime.utcnow)
class NodeSupplyBase(SQLModel):
    supply_type_id: Optional[int] = Field(default=None, index=True)
    farm_id: Optional[int] = Field(default=None, index=True)
    quantity: float = Field(default=0.0)
class NodeSupply(NodeSupplyBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: datetime = Field(default_factory=datetime.utcnow)