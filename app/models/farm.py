from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .farmer import NodeFarmer
    from .land import NodeLand
    from .account import NodeAccount
    from .farm_set import NodeFarmSet


# =========================================================
# FARM
# =========================================================

class NodeFarmBase(SQLModel):
    account_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeaccount.id"
    )

    main_land_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeland.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    farm_name: Optional[str] = None
    farm_type: Optional[str] = None
    farm_desc: Optional[str] = None

    size_type: Optional[str] = None
    certificate_number: Optional[str] = None

    display_order: Optional[int] = None

    foundation_date: Optional[datetime] = None
    close_date: Optional[datetime] = None

    farm_age: Optional[float] = None

    cnt_building: Optional[int] = None
    cnt_land: Optional[int] = None

    sum_area_land_m2: Optional[float] = None
    avg_annual_revenue: Optional[float] = None


class NodeFarm(NodeFarmBase, table=True):
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

    account: Optional["NodeAccount"] = Relationship(
        back_populates="farms"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="farms"
    )

    farmers: List["NodeFarmer"] = Relationship(
        back_populates="farm"
    )

    lands: List["NodeLand"] = Relationship(
        back_populates="farm",
        sa_relationship_kwargs={
            "foreign_keys": "[NodeLand.farm_id]"
        }
    )

    main_land: Optional["NodeLand"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeFarm.main_land_id]"
        }
    )

    buildings: List["NodeBuilding"] = Relationship(
        back_populates="farm",
        sa_relationship_kwargs={
            "foreign_keys": "[NodeBuilding.farm_id]"
        }
    )


# =========================================================
# BUILDING
# =========================================================

class NodeBuildingBase(SQLModel):
    farm_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarm.id"
    )

    land_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeland.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    building_type: Optional[str] = None
    building_name: Optional[str] = None
    building_desc: Optional[str] = None

    adress: Optional[str] = None
    official_no: Optional[str] = None

    num_storeys: Optional[int] = None

    length: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None

    area_m2: Optional[float] = None
    sum_m2: Optional[float] = None

    volume_m3: Optional[float] = None
    sum_volume_3: Optional[float] = None

    build_date: Optional[datetime] = None
    renovation_date: Optional[datetime] = None

    age: Optional[float] = None

    material_name: Optional[str] = None
    luminosity: Optional[str] = None
    thermal_sheathing: Optional[str] = None
    air_conditioning: Optional[str] = None


class NodeBuilding(NodeBuildingBase, table=True):
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

    farm: Optional["NodeFarm"] = Relationship(
        back_populates="buildings",
        sa_relationship_kwargs={
            "foreign_keys": "[NodeBuilding.farm_id]"
        }
    )

    land: Optional["NodeLand"] = Relationship(
        back_populates="buildings",
        sa_relationship_kwargs={
            "foreign_keys": "[NodeBuilding.land_id]"
        }
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="buildings"
    )