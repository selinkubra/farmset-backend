from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .user import NodePerson, NodeJuridical
    from .farm import NodeFarm
    from .farm_set import NodeFarmSet


class NodeAccountBase(SQLModel):
    person_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeperson.id"
    )

    juridical_id: Optional[int] = Field(
        default=None,
        foreign_key="nodejuridical.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    higher_account_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeaccount.id"
    )

    merged_account_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeaccount.id"
    )

    status: Optional[str] = None

    account_code: Optional[str] = None
    account_name: Optional[str] = None
    account_type: Optional[str] = None
    account_desc: Optional[str] = None

    display_order: Optional[int] = None

    create_date: Optional[datetime] = None
    close_date: Optional[datetime] = None


class NodeAccount(NodeAccountBase, table=True):
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

    person: Optional["NodePerson"] = Relationship(
        back_populates="accounts"
    )

    juridical: Optional["NodeJuridical"] = Relationship(
        back_populates="accounts"
    )

    farms: List["NodeFarm"] = Relationship(
        back_populates="account"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="accounts"
    )

    higher_account: Optional["NodeAccount"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeAccount.higher_account_id]",
            "remote_side": "[NodeAccount.id]",
        }
    )

    merged_account: Optional["NodeAccount"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeAccount.merged_account_id]",
            "remote_side": "[NodeAccount.id]",
        }
    )