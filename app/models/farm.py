# app/models/farm.py
from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class NodeFarmBase(SQLModel):
    name: str = Field(index=True)
    code: str = Field(unique=True, index=True)


class NodeFarm(NodeFarmBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Diğer modellerle (Land, Farmer vb.) ilişkiler buraya eklenebilir
    # lands: List["NodeLand"] = Relationship(back_populates="farm")
    # farmers: List["NodeFarmer"] = Relationship(back_populates="farm")