from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

class NodeUserBase(SQLModel):
    person_id: Optional[int] = Field(default=None, index=True) # Hangi gerçek kişiye ait
    user_type_id: Optional[int] = Field(default=None, index=True) # Admin, işçi
    status: Optional[str] = Field(default="ACTIVE")
    username: str = Field(unique=True, index=True)
    email: Optional[str] = Field(default=None, unique=True, index=True)

class NodeUser(NodeUserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) # Java'daki userId
    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)
class NodeUserLoginBase(SQLModel):
    user_id: Optional[int] = Field(default=None, index=True)
    password_hash: str
    last_login: Optional[datetime] = Field(default=None)
class NodeUserLogin(NodeUserLoginBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: datetime = Field(default_factory=datetime.utcnow)
class NodeUserTypeBase(SQLModel):
    name: str = Field(index=True) # Örn: Admin, Çiftçi
    description: Optional[str] = Field(default=None)
class NodeUserType(NodeUserTypeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: datetime = Field(default_factory=datetime.utcnow)
class NodePersonBase(SQLModel):
    first_name: str
    last_name: str
    identity_number: Optional[str] = Field(default=None, unique=True)
    birth_date: Optional[datetime] = Field(default=None)
class NodePerson(NodePersonBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: datetime = Field(default_factory=datetime.utcnow)
class NodePersonInfoBase(SQLModel):
    person_id: Optional[int] = Field(default=None, index=True)
    phone: Optional[str] = Field(default=None)
    address: Optional[str] = Field(default=None)
class NodePersonInfo(NodePersonInfoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: datetime = Field(default_factory=datetime.utcnow)
class NodeLanguageBase(SQLModel):
    code: str = Field(unique=True, index=True) # Örn: "TR", "EN"
    name: str
class NodeLanguage(NodeLanguageBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)