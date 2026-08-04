from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

# Base sınıf: Sadece verileri tanımlar
class NodePlantTypeBase(SQLModel):
    farm_set_id: Optional[int] = Field(default=None, index=True)
    status: Optional[str] = Field(default="ACTIVE")
    plant_type_name: str = Field(index=True)
    plant_type_desc: Optional[str] = Field(default=None)
    plant_type_code: Optional[str] = Field(default=None, index=True)
    scientific_name: Optional[str] = Field(default=None)
    scientific_long_name: Optional[str] = Field(default=None)
    biome_name: Optional[str] = Field(default=None)
    display_order: Optional[int] = Field(default=0)
    higher_plant_type: Optional[int] = Field(default=None, foreign_key="nodeplanttype.id")

# Table sınıfı: Veritabanı tablosunu oluşturur (Base'den miras alır)
class NodePlantType(NodePlantTypeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) # Java'daki plantTypeId
    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

class NodePlantBase(SQLModel):
    plant_type_id: Optional[int] = Field(default=None, index=True)
    farm_id: Optional[int] = Field(default=None, index=True)
    status: Optional[str] = Field(default="ACTIVE")
    planted_date: Optional[datetime] = Field(default=None)
class NodePlant(NodePlantBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)
class NodePlantTypeInfoBase(SQLModel):
    plant_type_id: Optional[int] = Field(default=None, index=True)
    growth_duration_days: Optional[int] = Field(default=0)
    water_requirement: Optional[str] = Field(default=None)
class NodePlantTypeInfo(NodePlantTypeInfoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: datetime = Field(default_factory=datetime.utcnow)
class NodeTreeBase(SQLModel):
    plant_id: Optional[int] = Field(default=None, index=True)
    height_cm: Optional[float] = Field(default=None)
    age_years: Optional[int] = Field(default=None)
class NodeTree(NodeTreeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: datetime = Field(default_factory=datetime.utcnow)


