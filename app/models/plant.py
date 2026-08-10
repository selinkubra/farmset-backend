from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .farm_set import NodeFarmSet


# =========================================================
# PLANT TYPE
# =========================================================

class NodePlantTypeBase(SQLModel):
    higher_plant_type: Optional[int] = Field(
        default=None,
        foreign_key="nodeplant.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    plant_type_name: Optional[str] = None
    plant_type_desc: Optional[str] = None
    plant_type_code: Optional[str] = None

    scientific_name: Optional[str] = None
    scientific_long_name: Optional[str] = None

    biome_name: Optional[str] = None

    display_order: Optional[int] = None


class NodePlantType(NodePlantTypeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    higher_plant: Optional["NodePlant"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodePlantType.higher_plant_type]"
        }
    )

    plants: List["NodePlant"] = Relationship(
        back_populates="plant_type",
        sa_relationship_kwargs={
            "foreign_keys": "[NodePlant.plant_type_id]"
        }
    )

    trees: List["NodeTree"] = Relationship(
        back_populates="plant_type",
        sa_relationship_kwargs={
            "foreign_keys": "[NodeTree.plant_type_id]"
        }
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="plant_types"
    )


# =========================================================
# PLANT TYPE INFO
# =========================================================

class NodePlantTypeInfoBase(SQLModel):
    plant_type_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeplanttype.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    seed_2_harvest_time_in_days: Optional[float] = None
    prod_per_acre: Optional[float] = None


class NodePlantTypeInfo(NodePlantTypeInfoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    plant_type: Optional["NodePlantType"] = Relationship()

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="plant_type_infos"
    )


# =========================================================
# PLANT
# =========================================================

class NodePlantBase(SQLModel):
    plant_type_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeplanttype.id"
    )

    land_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeland.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    plant_name: Optional[str] = None
    plant_desc: Optional[str] = None

    display_order: Optional[int] = None


class NodePlant(NodePlantBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    plant_type: Optional["NodePlantType"] = Relationship(
        back_populates="plants",
        sa_relationship_kwargs={
            "foreign_keys": "[NodePlant.plant_type_id]"
        }
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="plants"
    )


# =========================================================
# TREE
# =========================================================

class NodeTreeBase(SQLModel):
    land_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeland.id"
    )

    plant_type_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeplanttype.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    tree_name: Optional[str] = None
    tree_desc: Optional[str] = None

    display_order: Optional[int] = None

    seed_date: Optional[datetime] = None
    decease_date: Optional[datetime] = None

    age: Optional[float] = None

    last_measurement_date: Optional[datetime] = None

    height: Optional[float] = None
    tree_radius: Optional[float] = None

    stem_radius: Optional[float] = None
    stem_height: Optional[float] = None
    stem_volume_m3: Optional[float] = None
    stem_weight_kg: Optional[float] = None

    leaf_volume_m3: Optional[float] = None
    leaf_weight_kg: Optional[float] = None

    root_height: Optional[float] = None
    root_volume_m3: Optional[float] = None
    root_weight_kg: Optional[float] = None

    fruit_volume_m3: Optional[float] = None
    fruit_weight_kg: Optional[float] = None


class NodeTree(NodeTreeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    plant_type: Optional["NodePlantType"] = Relationship(
        back_populates="trees",
        sa_relationship_kwargs={
            "foreign_keys": "[NodeTree.plant_type_id]"
        }
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="trees"
    )