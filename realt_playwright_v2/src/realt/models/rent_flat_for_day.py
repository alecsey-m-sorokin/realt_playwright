from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class RentFlatForDayObject:
    object_type: str = "Квартира"
    object_rooms: str = "3"
    object_kitchen: str = "Отдельная кухня"
    object_repair: str = "Евроремонт"


@dataclass(frozen=True, slots=True)
class RentFlatForDayArea:
    area_total: str = "140"
    area_living: str = "80"
    area_kitchen: str = "25"


@dataclass(frozen=True, slots=True)
class RentFlatForDayHouse:
    floor: str = "9"
    floors_total: str = "16"
    year_built: str = "2010"


@dataclass(frozen=True, slots=True)
class RentFlatForDayCapacity:
    guests_max: str = "4"


@dataclass(frozen=True, slots=True)
class RentFlatForDayData:
    object: RentFlatForDayObject = field(default_factory=RentFlatForDayObject)
    area: RentFlatForDayArea = field(default_factory=RentFlatForDayArea)
    house: RentFlatForDayHouse = field(default_factory=RentFlatForDayHouse)
    capacity: RentFlatForDayCapacity = field(default_factory=RentFlatForDayCapacity)
