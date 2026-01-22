from dataclasses import dataclass
from typing import Optional


@dataclass
class FlatModel:

    @dataclass
    class Location:
        settlement: str
        street: Optional[str] = None
        house_number: Optional[str] = None
        building_number: Optional[str] = None

    @dataclass
    class Apartment:
        rooms: int
        separate_rooms: str
        storey: int

        @dataclass
        class Repair:
            Euro: Optional[str] = None

        @dataclass
        class Balcony:
            balcony: Optional[str] = None
            no: Optional[str] = None
            loggia: Optional[str] = None
            balcony_and_loggia: Optional[str] = None
            terrace: Optional[str] = None
