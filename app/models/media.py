from datetime import datetime
from typing import Optional, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .farm_set import NodeFarmSet


# =========================================================
# FARM MEDIA
# =========================================================

class NodeFarmMediaBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    media_id: Optional[int] = None


class NodeFarmMedia(NodeFarmMediaBase, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    creation_date: datetime = Field(
        default_factory=datetime.utcnow
    )

    modification_date: datetime = Field(
        default_factory=datetime.utcnow
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="farm_media"
    )


# =========================================================
# FARM DOC
# =========================================================

class NodeFarmDocBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    doc_id: Optional[int] = None


class NodeFarmDoc(NodeFarmDocBase, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    creation_date: datetime = Field(
        default_factory=datetime.utcnow
    )

    modification_date: datetime = Field(
        default_factory=datetime.utcnow
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="farm_docs"
    )