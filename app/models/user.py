from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .farmer import NodeFarmer
    from .account import NodeAccount
    from .farm_set import NodeFarmSet


# =========================================================
# USER TYPE
# =========================================================

class NodeUserTypeBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    user_type_name: Optional[str] = None
    user_type_desc: Optional[str] = None

    display_order: Optional[int] = None


class NodeUserType(NodeUserTypeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    users: List["NodeUser"] = Relationship(
        back_populates="user_type"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="user_types"
    )


# =========================================================
# LANGUAGE
# =========================================================

class NodeLanguageBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    language_name: Optional[str] = None
    language_desc: Optional[str] = None
    language_code: Optional[str] = None
    language_abbr: Optional[str] = None

    display_order: Optional[int] = None


class NodeLanguage(NodeLanguageBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="languages"
    )


# =========================================================
# PERSON
# =========================================================

class NodePersonBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    person_name: Optional[str] = None
    surname: Optional[str] = None
    middle_name: Optional[str] = None
    maiden_surname: Optional[str] = None
    full_name: Optional[str] = None

    gender: Optional[str] = None
    nationality: Optional[str] = None

    tckn: Optional[str] = None
    national_id: Optional[str] = None
    passport_id: Optional[str] = None

    birth_place: Optional[str] = None
    birth_date: Optional[datetime] = None

    display_order: Optional[int] = None


class NodePerson(NodePersonBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    farmer_records: List["NodeFarmer"] = Relationship(
        back_populates="person"
    )

    accounts: List["NodeAccount"] = Relationship(
        back_populates="person"
    )

    users: List["NodeUser"] = Relationship(
        back_populates="person"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="persons"
    )


# =========================================================
# USER
# =========================================================

class NodeUserBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    person_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeperson.id"
    )

    account_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeaccount.id"
    )

    user_type_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeusertype.id"
    )

    language_id: Optional[int] = Field(
        default=None,
        foreign_key="nodelanguage.id"
    )

    second_language_id: Optional[int] = Field(
        default=None,
        foreign_key="nodelanguage.id"
    )

    status: Optional[str] = None

    user_name: Optional[str] = None
    user_email: Optional[str] = None

    user_group: Optional[str] = None
    user_desc: Optional[str] = None
    user_port: Optional[str] = None

    read_only: Optional[str] = None

    encrypted_password: Optional[str] = None
    old_password_list: Optional[str] = None

    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    password_start_date: Optional[datetime] = None
    password_end_date: Optional[datetime] = None

    first_login_time: Optional[datetime] = None
    last_login_time: Optional[datetime] = None

    cnt_login: Optional[int] = None

    sum_duration_in_sec: Optional[float] = None
    sum_resource_in_tokens: Optional[float] = None

    display_order: Optional[int] = None


class NodeUser(NodeUserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    person: Optional["NodePerson"] = Relationship(
        back_populates="users"
    )

    account: Optional["NodeAccount"] = Relationship()

    user_type: Optional["NodeUserType"] = Relationship(
        back_populates="users"
    )

    language: Optional["NodeLanguage"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeUser.language_id]"
        }
    )

    second_language: Optional["NodeLanguage"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeUser.second_language_id]"
        }
    )

    logins: List["NodeUserLogin"] = Relationship(
        back_populates="user"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="users"
    )


# =========================================================
# USER LOGIN
# =========================================================

class NodeUserLoginBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    user_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeuser.id"
    )

    account_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeaccount.id"
    )

    language_id: Optional[int] = Field(
        default=None,
        foreign_key="nodelanguage.id"
    )

    second_language_id: Optional[int] = Field(
        default=None,
        foreign_key="nodelanguage.id"
    )

    status: Optional[str] = None

    login_code: Optional[str] = None

    host_ip: Optional[str] = None
    host_name: Optional[str] = None
    app_name: Optional[str] = None

    user_desc: Optional[str] = None
    read_only: Optional[str] = None

    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    sum_duration_in_sec: Optional[float] = None
    sum_resources_in_token: Optional[float] = None

    display_order: Optional[int] = None


class NodeUserLogin(NodeUserLoginBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    user: Optional["NodeUser"] = Relationship(
        back_populates="logins"
    )

    account: Optional["NodeAccount"] = Relationship()

    language: Optional["NodeLanguage"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeUserLogin.language_id]"
        }
    )

    second_language: Optional["NodeLanguage"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeUserLogin.second_language_id]"
        }
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="user_logins"
    )


# =========================================================
# PERSON INFO
# =========================================================

class NodePersonInfoBase(SQLModel):
    person_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeperson.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    living_place: Optional[str] = None
    living_place2: Optional[str] = None

    age: Optional[float] = None
    height_m: Optional[float] = None
    weight_kg: Optional[float] = None

    sport_status: Optional[str] = None
    sport_desc: Optional[str] = None

    marital_status: Optional[str] = None

    cnt_children: Optional[int] = None
    cnt_grand_children: Optional[int] = None

    parent_family_id: Optional[int] = None
    current_family_id: Optional[int] = None

    father_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeperson.id"
    )

    mother_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeperson.id"
    )

    spouse_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeperson.id"
    )

    profession: Optional[str] = None
    education_level: Optional[str] = None

    university_name: Optional[str] = None
    high_school_name: Optional[str] = None

    native_language: Optional[str] = None
    ethnic_language: Optional[str] = None

    foreign_language1: Optional[str] = None
    foreign_language2: Optional[str] = None
    foreign_language3: Optional[str] = None

    foreign_language_level1: Optional[str] = None
    foreign_language_level2: Optional[str] = None
    foreign_language_level3: Optional[str] = None

    working_status: Optional[str] = None
    work_title: Optional[str] = None
    working_time: Optional[str] = None
    working_place: Optional[str] = None

    retirement_status: Optional[str] = None
    retired_from: Optional[str] = None

    annual_income_salary: Optional[float] = None
    annual_income_rent: Optional[float] = None
    annual_income: Optional[float] = None

    retirement_date: Optional[datetime] = None
    expected_retirement_date: Optional[datetime] = None


class NodePersonInfo(NodePersonInfoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    person: Optional["NodePerson"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodePersonInfo.person_id]"
        }
    )

    father: Optional["NodePerson"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodePersonInfo.father_id]"
        }
    )

    mother: Optional["NodePerson"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodePersonInfo.mother_id]"
        }
    )

    spouse: Optional["NodePerson"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodePersonInfo.spouse_id]"
        }
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="person_infos"
    )


# =========================================================
# FAMILY
# =========================================================

class NodeFamilyBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    husband_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeperson.id"
    )

    wife_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeperson.id"
    )

    lived_building_id: Optional[int] = Field(
        default=None,
        foreign_key="nodebuilding.id"
    )

    status: Optional[str] = None

    family_code: Optional[str] = None
    family_name: Optional[str] = None
    family_type: Optional[str] = None
    family_desc: Optional[str] = None

    certificate_number: Optional[str] = None

    display_order: Optional[int] = None

    marriage_date: Optional[datetime] = None
    divorce_date: Optional[datetime] = None

    married_days: Optional[float] = None

    cnt_child: Optional[int] = None
    cnt_grand_child: Optional[int] = None
    cnt_resident: Optional[int] = None
    cnt_partial_resident: Optional[int] = None


class NodeFamily(NodeFamilyBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="families"
    )


# =========================================================
# JURIDICAL
# =========================================================

class NodeJuridicalBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    higher_juridical_id: Optional[int] = Field(
        default=None,
        foreign_key="nodejuridical.id"
    )

    merged_juridical_id: Optional[int] = Field(
        default=None,
        foreign_key="nodejuridical.id"
    )

    status: Optional[str] = None

    juridical_name: Optional[str] = None
    juridical_type: Optional[str] = None
    juridical_desc: Optional[str] = None
    juridical_abbr: Optional[str] = None
    juridical_code: Optional[str] = None

    tax_number: Optional[str] = None
    tax_office: Optional[str] = None

    province_name: Optional[str] = None
    district_name: Optional[str] = None

    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    display_order: Optional[int] = None

    page_number: Optional[int] = None
    line_number: Optional[int] = None
    word_number: Optional[int] = None


class NodeJuridical(NodeJuridicalBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    accounts: List["NodeAccount"] = Relationship(
        back_populates="juridical"
    )

    higher_juridical: Optional["NodeJuridical"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeJuridical.higher_juridical_id]",
            "remote_side": "[NodeJuridical.id]",
        }
    )

    merged_juridical: Optional["NodeJuridical"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeJuridical.merged_juridical_id]",
            "remote_side": "[NodeJuridical.id]",
        }
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="juridicals"
    )