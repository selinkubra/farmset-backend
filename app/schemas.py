# schemas.py
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

# ------------------------------------------------------------------
# 1. FARM SHAPES (Çiftlik Şemaları)
# ------------------------------------------------------------------
class FarmBase(BaseModel):
    name: str
    code: str

class FarmCreate(FarmBase):
    """Yeni çiftlik oluştururken istemcinin göndereceği veri."""
    pass

class FarmRead(FarmBase):
    """API'den istemciye (React Native) dönecek yanıt verisi."""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ------------------------------------------------------------------
# 2. LAND SHAPES (Arazi Şemaları)
# ------------------------------------------------------------------
class LandBase(BaseModel):
    title: str
    latitude: float
    longitude: float
    altitude: float = 0.0
    area_sqm: float = 0.0
    perimeter_m: float = 0.0

class LandCreate(LandBase):
    farm_id: int

class LandRead(LandBase):
    id: int
    farm_id: Optional[int] = None

    class Config:
        from_attributes = True


# ------------------------------------------------------------------
# 3. FARMER SHAPES (Çiftçi Şemaları)
# ------------------------------------------------------------------
class FarmerBase(BaseModel):
    first_name: str
    last_name: str
    experience_years: int = 0

class FarmerCreate(FarmerBase):
    farm_id: int

class FarmerRead(FarmerBase):
    id: int
    hired_at: Optional[datetime] = None
    farm_id: Optional[int] = None

    class Config:
        from_attributes = True