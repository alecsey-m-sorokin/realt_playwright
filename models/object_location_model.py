from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class ObjectLocationModel:
    """DTO для хранения данных локации объекта."""
    settlement: str
    settlement_name: str
    street: Optional[str]
    street_name: Optional[str]
    house_number: Optional[str]
    building_number: Optional[str] = None
