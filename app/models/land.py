from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .farm import NodeFarm, NodeBuilding
    from .farm_set import NodeFarmSet


# =========================================================
# KML
# =========================================================

class NodeKmlBase(SQLModel):
    kmz_id: Optional[int] = None

    land_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeland.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    kml_type: Optional[str] = None
    kml_name: Optional[str] = None
    kml_desc: Optional[str] = None

    create_date: Optional[datetime] = None

    display_order: Optional[int] = None

    perimeter_m: Optional[float] = None
    area_m2: Optional[float] = None


class NodeKml(NodeKmlBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="kml_files"
    )


# =========================================================
# KMZ
# =========================================================

class NodeKmzBase(SQLModel):
    land_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeland.id"
    )

    doc_id: Optional[int] = None
    doc_set_id: Optional[int] = None

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    kmz_type: Optional[str] = None
    kmz_name: Optional[str] = None
    kmz_desc: Optional[str] = None

    display_order: Optional[int] = None

    cnt_kml: Optional[int] = None

    sum_perimeter_m: Optional[float] = None
    sum_area_m2: Optional[float] = None


class NodeKmz(NodeKmzBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="kmz_files"
    )


# =========================================================
# LAND
# =========================================================

class NodeLandBase(SQLModel):
    farm_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarm.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    land_name: Optional[str] = None
    land_type: Optional[str] = None
    land_desc: Optional[str] = None

    length: Optional[float] = None
    width: Optional[float] = None

    latitude: Optional[float] = None
    longitude: Optional[float] = None

    avg_altitude: Optional[float] = None

    perimeter_m: Optional[float] = None
    area_m2: Optional[float] = None

    display_order: Optional[int] = None


class NodeLand(NodeLandBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    farm: Optional["NodeFarm"] = Relationship(
        back_populates="lands",
        sa_relationship_kwargs={
            "foreign_keys": "[NodeLand.farm_id]"
        }
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="lands"
    )

    buildings: List["NodeBuilding"] = Relationship(
        back_populates="land",
        sa_relationship_kwargs={
            "foreign_keys": "[NodeBuilding.land_id]"
        }
    )