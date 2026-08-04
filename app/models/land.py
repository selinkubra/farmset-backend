# app/models/land.py
from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


# --- KML / KMZ Harita Veri Modelleri ---
class NodeKmlBase(SQLModel):
    file_name: str
    file_path: str
    content: Optional[str] = None


class NodeKml(NodeKmlBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    land_id: Optional[int] = Field(default=None, foreign_key="nodeland.id")


class NodeKmzBase(SQLModel):
    file_name: str
    file_path: str


class NodeKmz(NodeKmzBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    land_id: Optional[int] = Field(default=None, foreign_key="nodeland.id")


# --- Mahsul / Ürün Modeli ---
class NodeCropBase(SQLModel):
    name: str = Field(index=True)
    season: Optional[str] = None


class NodeCrop(NodeCropBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    land_id: Optional[int] = Field(default=None, foreign_key="nodeland.id")


# --- Arazi Modeli ---
class NodeLandBase(SQLModel):
    name: str = Field(index=True)
    ada: Optional[str] = None
    parsel: Optional[str] = None
    area_sqm: Optional[float] = None  # Metrekare cinsinden alan


class NodeLand(NodeLandBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Çiftlik ilişkisi (Foreign Key)
    farm_id: Optional[int] = Field(default=None, foreign_key="nodefarm.id")