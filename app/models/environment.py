from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .farm_set import NodeFarmSet


# =========================================================
# SOIL TYPE
# =========================================================

class NodeSoilTypeBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    soil_type_name: Optional[str] = None
    soil_type_desc: Optional[str] = None
    soil_type_code: Optional[str] = None

    display_order: Optional[int] = None


class NodeSoilType(NodeSoilTypeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    soils: List["NodeSoil"] = Relationship(
        back_populates="soil_type"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="soil_types"
    )


# =========================================================
# SOIL
# =========================================================

class NodeSoilBase(SQLModel):
    soil_type_id: Optional[int] = Field(
        default=None,
        foreign_key="nodesoiltype.id"
    )

    land_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeland.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    soil_name: Optional[str] = None
    soil_desc: Optional[str] = None
    soil_code: Optional[str] = None

    display_order: Optional[int] = None


class NodeSoil(NodeSoilBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    soil_type: Optional["NodeSoilType"] = Relationship(
        back_populates="soils"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="soils"
    )


# =========================================================
# SEASON
# =========================================================

class NodeSeasonBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    previous_season_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeseason.id"
    )

    next_season_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeseason.id"
    )

    season_name: Optional[str] = None
    season_type: Optional[str] = None
    season_code: Optional[str] = None
    season_desc: Optional[str] = None

    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    display_order: Optional[int] = None
    duration_in_days: Optional[float] = None


class NodeSeason(NodeSeasonBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    previous_season: Optional["NodeSeason"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeSeason.previous_season_id]",
            "remote_side": "[NodeSeason.id]",
        }
    )

    next_season: Optional["NodeSeason"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeSeason.next_season_id]",
            "remote_side": "[NodeSeason.id]",
        }
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="seasons"
    )


# =========================================================
# CALENDAR
# =========================================================

class NodeCalendarBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    calendar_name: Optional[str] = None
    calendar_type: Optional[str] = None
    calendar_desc: Optional[str] = None

    starting_of_day: Optional[str] = None
    starting_of_week: Optional[str] = None

    display_order: Optional[int] = None


class NodeCalendar(NodeCalendarBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    calendar_days: List["NodeCalendarDay"] = Relationship(
        back_populates="calendar"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="calendars"
    )


# =========================================================
# CALENDAR DAY
# =========================================================

class NodeCalendarDayBase(SQLModel):
    calendar_id: Optional[int] = Field(
        default=None,
        foreign_key="nodecalendar.id"
    )

    previous_day_id: Optional[int] = Field(
        default=None,
        foreign_key="nodecalendarday.id"
    )

    next_day_id: Optional[int] = Field(
        default=None,
        foreign_key="nodecalendarday.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    day_name: Optional[str] = None
    day_yyyymmdd: Optional[str] = None

    holiday_name: Optional[str] = None
    holiday_day: Optional[str] = None

    calendar_date: Optional[datetime] = None

    display_order: Optional[int] = None

    day_of_week: Optional[int] = None
    day_of_year: Optional[int] = None


class NodeCalendarDay(NodeCalendarDayBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    calendar: Optional["NodeCalendar"] = Relationship(
        back_populates="calendar_days",
        sa_relationship_kwargs={
            "foreign_keys": "[NodeCalendarDay.calendar_id]"
        }
    )

    previous_day: Optional["NodeCalendarDay"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeCalendarDay.previous_day_id]",
            "remote_side": "[NodeCalendarDay.id]",
        }
    )

    next_day: Optional["NodeCalendarDay"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeCalendarDay.next_day_id]",
            "remote_side": "[NodeCalendarDay.id]",
        }
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="calendar_days"
    )