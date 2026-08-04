# app/models/farmer.py
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.farm import NodeFarm


# --- ÇİFTÇİ / BİREYSEL MODELLER ---
class NodeFarmerBase(SQLModel):
    first_name: str
    last_name: str
    identity_number: Optional[str] = Field(default=None, unique=True, index=True)  # TC Kimlik No
    phone: Optional[str] = None
    email: Optional[str] = None


class NodeFarmer(NodeFarmerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Düzeltildi: primary_key
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Çiftlik ile Foreign Key ve Relationship Bağlantısı
    farm_id: Optional[int] = Field(default=None, foreign_key="nodefarm.id")
    farm: Optional["NodeFarm"] = Relationship(back_populates="farmers")


# --- TÜZEL KİŞİLİK / ŞİRKET MODELLERİ ---
class NodeJuridicalBase(SQLModel):
    company_name: str
    tax_number: str = Field(unique=True, index=True)
    tax_office: Optional[str] = None


class NodeJuridical(NodeJuridicalBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Çiftlik veya Çiftçi İlişkisi
    farm_id: Optional[int] = Field(default=None, foreign_key="nodefarm.id")
    farm: Optional["NodeFarm"] = Relationship(back_populates="juridical")