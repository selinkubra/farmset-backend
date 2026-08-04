from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

# 1. Toprak Tipleri (Soil Type)
class NodeSoilTypeBase(SQLModel):
    farm_set_id: Optional[int] = Field(default=None, index=True)
    soil_type_name: str = Field(index=True)
    soil_type_desc: Optional[str] = Field(default=None)
    display_order: Optional[int] = Field(default=0)

class NodeSoilType(NodeSoilTypeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) # Java'daki soilTypeId
    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)


# 2. Üretim Sezonu / Dönemi (Season)
class NodeSeasonBase(SQLModel):
    farm_set_id: Optional[int] = Field(default=None, index=True)
    status: Optional[str] = Field(default="ACTIVE")
    season_name: str = Field(index=True) # Örn: "2026 İlkbahar Koza Dönemi"
    start_date: Optional[datetime] = Field(default=None)
    end_date: Optional[datetime] = Field(default=None)

class NodeSeason(NodeSeasonBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) # Java'daki seasonId
    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

class NodeSoilBase(SQLModel):
    soil_type_id: Optional[int] = Field(default=None, index=True)
    land_id: Optional[int] = Field(default=None, index=True)
    ph_level: Optional[float] = Field(default=None)
    status: Optional[str] = Field(default="ACTIVE")
class NodeSoil(NodeSoilBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)
