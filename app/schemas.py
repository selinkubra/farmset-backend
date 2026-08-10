from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


# =========================================================
# FARM SCHEMAS
# =========================================================

class FarmBase(BaseModel):
    account_id: Optional[int] = None
    main_land_id: Optional[int] = None
    farm_set_id: Optional[int] = None

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


class FarmCreate(FarmBase):
    pass


class FarmUpdate(BaseModel):
    account_id: Optional[int] = None
    main_land_id: Optional[int] = None
    farm_set_id: Optional[int] = None

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


class FarmRead(FarmBase):
    id: int

    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# LAND SCHEMAS
# =========================================================

class LandBase(BaseModel):
    farm_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    land_name: Optional[str] = None
    land_type: Optional[str] = None
    land_desc: Optional[str] = None

    length: Optional[float] = None
    width: Optional[float] = None

    latitude: Optional[float] = None
    longitude: Optional[float] = None

    avg_altitude: Optional[float] = None

    perimeter_m: Optional[float] = None
    area_m2: Optional[float] = None

    display_order: Optional[int] = None


class LandCreate(LandBase):
    pass


class LandUpdate(BaseModel):
    farm_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    land_name: Optional[str] = None
    land_type: Optional[str] = None
    land_desc: Optional[str] = None

    length: Optional[float] = None
    width: Optional[float] = None

    latitude: Optional[float] = None
    longitude: Optional[float] = None

    avg_altitude: Optional[float] = None

    perimeter_m: Optional[float] = None
    area_m2: Optional[float] = None

    display_order: Optional[int] = None


class LandRead(LandBase):
    id: int

    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# FARMER SCHEMAS
# =========================================================

class FarmerBase(BaseModel):
    farm_id: Optional[int] = None
    person_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    farmer_name: Optional[str] = None
    farmer_code: Optional[str] = None
    farmer_type: Optional[str] = None
    farmer_desc: Optional[str] = None

    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    display_order: Optional[int] = None
    experience_year: Optional[float] = None


class FarmerCreate(FarmerBase):
    pass


class FarmerUpdate(BaseModel):
    farm_id: Optional[int] = None
    person_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    farmer_name: Optional[str] = None
    farmer_code: Optional[str] = None
    farmer_type: Optional[str] = None
    farmer_desc: Optional[str] = None

    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    display_order: Optional[int] = None
    experience_year: Optional[float] = None


class FarmerRead(FarmerBase):
    id: int

    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)

# =========================================================
# USER SCHEMAS
# =========================================================

class UserBase(BaseModel):
    farm_set_id: Optional[int] = None
    person_id: Optional[int] = None
    account_id: Optional[int] = None
    user_type_id: Optional[int] = None

    language_id: Optional[int] = None
    second_language_id: Optional[int] = None

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


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    farm_set_id: Optional[int] = None
    person_id: Optional[int] = None
    account_id: Optional[int] = None
    user_type_id: Optional[int] = None

    language_id: Optional[int] = None
    second_language_id: Optional[int] = None

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


class UserRead(UserBase):
    id: int

    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)

# =========================================================
# PLANT TYPE SCHEMAS
# =========================================================

class PlantTypeBase(BaseModel):
    higher_plant_type: Optional[int] = None
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    plant_type_name: Optional[str] = None
    plant_type_desc: Optional[str] = None
    plant_type_code: Optional[str] = None

    scientific_name: Optional[str] = None
    scientific_long_name: Optional[str] = None

    biome_name: Optional[str] = None

    display_order: Optional[int] = None


class PlantTypeCreate(PlantTypeBase):
    pass


class PlantTypeUpdate(BaseModel):
    higher_plant_type: Optional[int] = None
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    plant_type_name: Optional[str] = None
    plant_type_desc: Optional[str] = None
    plant_type_code: Optional[str] = None

    scientific_name: Optional[str] = None
    scientific_long_name: Optional[str] = None

    biome_name: Optional[str] = None

    display_order: Optional[int] = None


class PlantTypeRead(PlantTypeBase):
    id: int
    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# PLANT SCHEMAS
# =========================================================

class PlantBase(BaseModel):
    plant_type_id: Optional[int] = None
    land_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    plant_name: Optional[str] = None
    plant_desc: Optional[str] = None

    display_order: Optional[int] = None


class PlantCreate(PlantBase):
    pass


class PlantUpdate(BaseModel):
    plant_type_id: Optional[int] = None
    land_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    plant_name: Optional[str] = None
    plant_desc: Optional[str] = None

    display_order: Optional[int] = None


class PlantRead(PlantBase):
    id: int
    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# PLANT TYPE INFO SCHEMAS
# =========================================================

class PlantTypeInfoBase(BaseModel):
    plant_type_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    seed_2_harvest_time_in_days: Optional[float] = None
    prod_per_acre: Optional[float] = None


class PlantTypeInfoCreate(PlantTypeInfoBase):
    pass


class PlantTypeInfoUpdate(BaseModel):
    plant_type_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    seed_2_harvest_time_in_days: Optional[float] = None
    prod_per_acre: Optional[float] = None


class PlantTypeInfoRead(PlantTypeInfoBase):
    id: int
    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# TREE SCHEMAS
# =========================================================

class TreeBase(BaseModel):
    land_id: Optional[int] = None
    plant_type_id: Optional[int] = None
    farm_set_id: Optional[int] = None

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


class TreeCreate(TreeBase):
    pass


class TreeUpdate(BaseModel):
    land_id: Optional[int] = None
    plant_type_id: Optional[int] = None
    farm_set_id: Optional[int] = None

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


class TreeRead(TreeBase):
    id: int
    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)

# =========================================================
# VEHICLE TYPE SCHEMAS
# =========================================================

class VehicleTypeBase(BaseModel):
    farm_set_id: Optional[int] = None
    status: Optional[str] = None

    vehicle_type_name: Optional[str] = None
    vehicle_type_desc: Optional[str] = None
    vehicle_type_code: Optional[str] = None

    display_order: Optional[int] = None


class VehicleTypeCreate(VehicleTypeBase):
    pass


class VehicleTypeUpdate(BaseModel):
    farm_set_id: Optional[int] = None
    status: Optional[str] = None

    vehicle_type_name: Optional[str] = None
    vehicle_type_desc: Optional[str] = None
    vehicle_type_code: Optional[str] = None

    display_order: Optional[int] = None


class VehicleTypeRead(VehicleTypeBase):
    id: int
    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# VEHICLE SCHEMAS
# =========================================================

class VehicleBase(BaseModel):
    farm_id: Optional[int] = None
    vehicle_type_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    vehicle_name: Optional[str] = None
    vehicle_desc: Optional[str] = None

    plate_number: Optional[str] = None

    brand_name: Optional[str] = None
    model_name: Optional[str] = None
    model_year: Optional[int] = None

    serial_number: Optional[str] = None
    engine_number: Optional[str] = None
    chassis_number: Optional[str] = None

    purchase_date: Optional[datetime] = None
    sale_date: Optional[datetime] = None

    purchase_price: Optional[float] = None
    sale_price: Optional[float] = None
    current_value: Optional[float] = None

    display_order: Optional[int] = None


class VehicleCreate(VehicleBase):
    pass


class VehicleUpdate(BaseModel):
    farm_id: Optional[int] = None
    vehicle_type_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    vehicle_name: Optional[str] = None
    vehicle_desc: Optional[str] = None

    plate_number: Optional[str] = None

    brand_name: Optional[str] = None
    model_name: Optional[str] = None
    model_year: Optional[int] = None

    serial_number: Optional[str] = None
    engine_number: Optional[str] = None
    chassis_number: Optional[str] = None

    purchase_date: Optional[datetime] = None
    sale_date: Optional[datetime] = None

    purchase_price: Optional[float] = None
    sale_price: Optional[float] = None
    current_value: Optional[float] = None

    display_order: Optional[int] = None


class VehicleRead(VehicleBase):
    id: int
    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# TOOL TYPE SCHEMAS
# =========================================================

class ToolTypeBase(BaseModel):
    farm_set_id: Optional[int] = None
    status: Optional[str] = None

    tool_type_name: Optional[str] = None
    tool_type_desc: Optional[str] = None
    tool_type_code: Optional[str] = None

    display_order: Optional[int] = None


class ToolTypeCreate(ToolTypeBase):
    pass


class ToolTypeUpdate(BaseModel):
    farm_set_id: Optional[int] = None
    status: Optional[str] = None

    tool_type_name: Optional[str] = None
    tool_type_desc: Optional[str] = None
    tool_type_code: Optional[str] = None

    display_order: Optional[int] = None


class ToolTypeRead(ToolTypeBase):
    id: int
    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# TOOL SCHEMAS
# =========================================================

class ToolBase(BaseModel):
    farm_id: Optional[int] = None
    tool_type_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    tool_name: Optional[str] = None
    tool_desc: Optional[str] = None

    brand_name: Optional[str] = None
    model_name: Optional[str] = None
    serial_number: Optional[str] = None

    purchase_date: Optional[datetime] = None
    sale_date: Optional[datetime] = None

    purchase_price: Optional[float] = None
    sale_price: Optional[float] = None
    current_value: Optional[float] = None

    display_order: Optional[int] = None


class ToolCreate(ToolBase):
    pass


class ToolUpdate(BaseModel):
    farm_id: Optional[int] = None
    tool_type_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    tool_name: Optional[str] = None
    tool_desc: Optional[str] = None

    brand_name: Optional[str] = None
    model_name: Optional[str] = None
    serial_number: Optional[str] = None

    purchase_date: Optional[datetime] = None
    sale_date: Optional[datetime] = None

    purchase_price: Optional[float] = None
    sale_price: Optional[float] = None
    current_value: Optional[float] = None

    display_order: Optional[int] = None


class ToolRead(ToolBase):
    id: int
    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# SUPPLY TYPE SCHEMAS
# =========================================================

class SupplyTypeBase(BaseModel):
    farm_set_id: Optional[int] = None
    status: Optional[str] = None

    supply_type_name: Optional[str] = None
    supply_type_desc: Optional[str] = None
    supply_type_code: Optional[str] = None

    unit_name: Optional[str] = None

    display_order: Optional[int] = None


class SupplyTypeCreate(SupplyTypeBase):
    pass


class SupplyTypeUpdate(BaseModel):
    farm_set_id: Optional[int] = None
    status: Optional[str] = None

    supply_type_name: Optional[str] = None
    supply_type_desc: Optional[str] = None
    supply_type_code: Optional[str] = None

    unit_name: Optional[str] = None

    display_order: Optional[int] = None


class SupplyTypeRead(SupplyTypeBase):
    id: int
    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# SUPPLY SCHEMAS
# =========================================================

class SupplyBase(BaseModel):
    farm_id: Optional[int] = None
    supply_type_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    supply_name: Optional[str] = None
    supply_desc: Optional[str] = None

    quantity: Optional[float] = None
    unit_price: Optional[float] = None
    total_value: Optional[float] = None

    purchase_date: Optional[datetime] = None
    expiration_date: Optional[datetime] = None

    display_order: Optional[int] = None


class SupplyCreate(SupplyBase):
    pass


class SupplyUpdate(BaseModel):
    farm_id: Optional[int] = None
    supply_type_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    supply_name: Optional[str] = None
    supply_desc: Optional[str] = None

    quantity: Optional[float] = None
    unit_price: Optional[float] = None
    total_value: Optional[float] = None

    purchase_date: Optional[datetime] = None
    expiration_date: Optional[datetime] = None

    display_order: Optional[int] = None


class SupplyRead(SupplyBase):
    id: int
    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)

# =========================================================
# SOIL TYPE SCHEMAS
# =========================================================

class SoilTypeBase(BaseModel):
    farm_set_id: Optional[int] = None

    soil_type_name: Optional[str] = None
    soil_type_desc: Optional[str] = None
    soil_type_code: Optional[str] = None

    display_order: Optional[int] = None


class SoilTypeCreate(SoilTypeBase):
    pass


class SoilTypeUpdate(BaseModel):
    farm_set_id: Optional[int] = None

    soil_type_name: Optional[str] = None
    soil_type_desc: Optional[str] = None
    soil_type_code: Optional[str] = None

    display_order: Optional[int] = None


class SoilTypeRead(SoilTypeBase):
    id: int
    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# SOIL SCHEMAS
# =========================================================

class SoilBase(BaseModel):
    soil_type_id: Optional[int] = None
    land_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    soil_name: Optional[str] = None
    soil_desc: Optional[str] = None
    soil_code: Optional[str] = None

    display_order: Optional[int] = None


class SoilCreate(SoilBase):
    pass


class SoilUpdate(BaseModel):
    soil_type_id: Optional[int] = None
    land_id: Optional[int] = None
    farm_set_id: Optional[int] = None

    soil_name: Optional[str] = None
    soil_desc: Optional[str] = None
    soil_code: Optional[str] = None

    display_order: Optional[int] = None


class SoilRead(SoilBase):
    id: int
    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# SEASON SCHEMAS
# =========================================================

class SeasonBase(BaseModel):
    farm_set_id: Optional[int] = None

    previous_season_id: Optional[int] = None
    next_season_id: Optional[int] = None

    season_name: Optional[str] = None
    season_type: Optional[str] = None
    season_code: Optional[str] = None
    season_desc: Optional[str] = None

    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    display_order: Optional[int] = None
    duration_in_days: Optional[float] = None


class SeasonCreate(SeasonBase):
    pass


class SeasonUpdate(BaseModel):
    farm_set_id: Optional[int] = None

    previous_season_id: Optional[int] = None
    next_season_id: Optional[int] = None

    season_name: Optional[str] = None
    season_type: Optional[str] = None
    season_code: Optional[str] = None
    season_desc: Optional[str] = None

    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    display_order: Optional[int] = None
    duration_in_days: Optional[float] = None


class SeasonRead(SeasonBase):
    id: int
    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# CALENDAR SCHEMAS
# =========================================================

class CalendarBase(BaseModel):
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    calendar_name: Optional[str] = None
    calendar_type: Optional[str] = None
    calendar_desc: Optional[str] = None

    starting_of_day: Optional[str] = None
    starting_of_week: Optional[str] = None

    display_order: Optional[int] = None


class CalendarCreate(CalendarBase):
    pass


class CalendarUpdate(BaseModel):
    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    calendar_name: Optional[str] = None
    calendar_type: Optional[str] = None
    calendar_desc: Optional[str] = None

    starting_of_day: Optional[str] = None
    starting_of_week: Optional[str] = None

    display_order: Optional[int] = None


class CalendarRead(CalendarBase):
    id: int
    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# CALENDAR DAY SCHEMAS
# =========================================================

class CalendarDayBase(BaseModel):
    calendar_id: Optional[int] = None

    previous_day_id: Optional[int] = None
    next_day_id: Optional[int] = None

    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    day_name: Optional[str] = None
    day_yyyymmdd: Optional[str] = None

    holiday_name: Optional[str] = None
    holiday_day: Optional[str] = None

    calendar_date: Optional[datetime] = None

    display_order: Optional[int] = None

    day_of_week: Optional[int] = None
    day_of_year: Optional[int] = None


class CalendarDayCreate(CalendarDayBase):
    pass


class CalendarDayUpdate(BaseModel):
    calendar_id: Optional[int] = None

    previous_day_id: Optional[int] = None
    next_day_id: Optional[int] = None

    farm_set_id: Optional[int] = None

    status: Optional[str] = None

    day_name: Optional[str] = None
    day_yyyymmdd: Optional[str] = None

    holiday_name: Optional[str] = None
    holiday_day: Optional[str] = None

    calendar_date: Optional[datetime] = None

    display_order: Optional[int] = None

    day_of_week: Optional[int] = None
    day_of_year: Optional[int] = None


class CalendarDayRead(CalendarDayBase):
    id: int
    creation_date: datetime
    modification_date: datetime

    model_config = ConfigDict(from_attributes=True)