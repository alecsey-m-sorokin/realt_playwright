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
