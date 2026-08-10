from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .account import NodeAccount
    from .farm import NodeFarm, NodeBuilding
    from .farmer import NodeFarmer
    from .land import NodeLand, NodeKml, NodeKmz
    from .user import (
        NodeUser,
        NodeUserLogin,
        NodeUserType,
        NodePerson,
        NodePersonInfo,
        NodeLanguage,
        NodeFamily,
        NodeJuridical,
    )
    from .plant import (
        NodePlant,
        NodePlantType,
        NodePlantTypeInfo,
        NodeTree,
    )
    from .inventory import (
        NodeVehicle,
        NodeVehicleType,
        NodeToolType,
        NodeSupply,
        NodeSupplyType,
    )
    from .environment import (
        NodeSoil,
        NodeSoilType,
        NodeSeason,
        NodeCalendar,
        NodeCalendarDay,
    )
    from .finance import (
        NodeBankAccount,
        NodeContract,
        NodeContractType,
    )
    from .media import (
        NodeFarmDoc,
        NodeFarmMedia,
    )


# =========================================================
# FARM SET
# =========================================================

class NodeFarmSetBase(SQLModel):
    file_set_id: Optional[int] = None

    farm_set_name: Optional[str] = None
    farm_set_desc: Optional[str] = None
    source_desc: Optional[str] = None


class NodeFarmSet(NodeFarmSetBase, table=True):
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

    accounts: List["NodeAccount"] = Relationship(
        back_populates="farm_set"
    )

    farms: List["NodeFarm"] = Relationship(
        back_populates="farm_set"
    )

    buildings: List["NodeBuilding"] = Relationship(
        back_populates="farm_set"
    )

    farmers: List["NodeFarmer"] = Relationship(
        back_populates="farm_set"
    )

    lands: List["NodeLand"] = Relationship(
        back_populates="farm_set"
    )

    kml_files: List["NodeKml"] = Relationship(
        back_populates="farm_set"
    )

    kmz_files: List["NodeKmz"] = Relationship(
        back_populates="farm_set"
    )

    users: List["NodeUser"] = Relationship(
        back_populates="farm_set"
    )

    user_logins: List["NodeUserLogin"] = Relationship(
        back_populates="farm_set"
    )

    user_types: List["NodeUserType"] = Relationship(
        back_populates="farm_set"
    )

    persons: List["NodePerson"] = Relationship(
        back_populates="farm_set"
    )

    person_infos: List["NodePersonInfo"] = Relationship(
        back_populates="farm_set"
    )

    languages: List["NodeLanguage"] = Relationship(
        back_populates="farm_set"
    )

    families: List["NodeFamily"] = Relationship(
        back_populates="farm_set"
    )

    juridicals: List["NodeJuridical"] = Relationship(
        back_populates="farm_set"
    )

    plants: List["NodePlant"] = Relationship(
        back_populates="farm_set"
    )

    plant_types: List["NodePlantType"] = Relationship(
        back_populates="farm_set"
    )

    plant_type_infos: List["NodePlantTypeInfo"] = Relationship(
        back_populates="farm_set"
    )

    trees: List["NodeTree"] = Relationship(
        back_populates="farm_set"
    )

    vehicles: List["NodeVehicle"] = Relationship(
        back_populates="farm_set"
    )

    vehicle_types: List["NodeVehicleType"] = Relationship(
        back_populates="farm_set"
    )

    tool_types: List["NodeToolType"] = Relationship(
        back_populates="farm_set"
    )

    supplies: List["NodeSupply"] = Relationship(
        back_populates="farm_set"
    )

    supply_types: List["NodeSupplyType"] = Relationship(
        back_populates="farm_set"
    )

    soils: List["NodeSoil"] = Relationship(
        back_populates="farm_set"
    )

    soil_types: List["NodeSoilType"] = Relationship(
        back_populates="farm_set"
    )

    seasons: List["NodeSeason"] = Relationship(
        back_populates="farm_set"
    )

    calendars: List["NodeCalendar"] = Relationship(
        back_populates="farm_set"
    )

    calendar_days: List["NodeCalendarDay"] = Relationship(
        back_populates="farm_set"
    )

    bank_accounts: List["NodeBankAccount"] = Relationship(
        back_populates="farm_set"
    )

    contracts: List["NodeContract"] = Relationship(
        back_populates="farm_set"
    )

    contract_types: List["NodeContractType"] = Relationship(
        back_populates="farm_set"
    )

    farm_docs: List["NodeFarmDoc"] = Relationship(
        back_populates="farm_set"
    )

    farm_media: List["NodeFarmMedia"] = Relationship(
        back_populates="farm_set"
    )