from datetime import datetime
from typing import Optional, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .farm import NodeFarm
    from .user import NodePerson
    from .farm_set import NodeFarmSet


class NodeFarmerBase(SQLModel):
    farm_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarm.id"
    )

    person_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeperson.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    farmer_name: Optional[str] = None
    farmer_code: Optional[str] = None
    farmer_type: Optional[str] = None
    farmer_desc: Optional[str] = None

    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    display_order: Optional[int] = None
    experience_year: Optional[float] = None


class NodeFarmer(NodeFarmerBase, table=True):
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
        back_populates="farmers"
    )

    person: Optional["NodePerson"] = Relationship(
        back_populates="farmer_records"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="farmers"
    )