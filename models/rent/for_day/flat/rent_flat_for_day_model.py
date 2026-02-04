from dataclasses import dataclass, field
from typing import Optional

@dataclass(frozen=True)
class RentFlatForDayModel:
    """DTO для хранения данных аренды квартира посуточная."""

    @dataclass
    class Object:
        object_type: Optional[str] = 'Квартира'
        object_rooms: Optional[str] = '3'
        object_kitchen: Optional[str] = 'Отдельная кухня'
        object_repair: Optional[str] = 'Евроремонт'

    object: Object = field(default_factory=Object)

    @dataclass
    class Area:
        area_total: Optional[str] = '140'
        area_living: Optional[str] = '80'
        area_kitchen: Optional[str] = '25'

    area: Area = field(default_factory=Area)
