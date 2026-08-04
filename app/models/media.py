# app/models/media.py
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


# --- Çiftlik Medya ve Belge Modelleri ---
class NodeFarmMediaBase(SQLModel):
    file_name: str
    file_path: str
    media_type: Optional[str] = None  # Resim, Video vb.


class NodeFarmMedia(NodeFarmMediaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    farm_id: Optional[int] = Field(default=None, foreign_key="nodefarm.id")


class NodeFarmDocBase(SQLModel):
    title: str
    file_path: str
    doc_type: Optional[str] = None  # Tapu, Ruhsat, Sözleşme vb.


class NodeFarmDoc(NodeFarmDocBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    farm_id: Optional[int] = Field(default=None, foreign_key="nodefarm.id")


# --- Ekipman Modeli ---
class NodeEquipmentBase(SQLModel):
    name: str = Field(index=True)
    model_year: Optional[int] = None
    serial_number: Optional[str] = None


class NodeEquipment(NodeEquipmentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    farm_id: Optional[int] = Field(default=None, foreign_key="nodefarm.id")


# --- Sistem Log Modeli ---
class NodeLogBase(SQLModel):
    action: str
    details: Optional[str] = None


class NodeLog(NodeLogBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)