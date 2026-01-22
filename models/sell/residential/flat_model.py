from dataclasses import dataclass
from typing import Optional


@dataclass
class FlatModel:

    @dataclass
    class Location:
        """Адрес"""
        settlement: str
        street: Optional[str] = None
        house_number: Optional[str] = None
        building_number: Optional[str] = None

    @dataclass
    class Apartment:
        """Комнат"""
        rooms: int
        separate_rooms: str
        storey: int

        @dataclass
        class Repair:
            """Ремонт"""
            Euro: Optional[str] = None

        @dataclass
        class Balcony:
            """Балконов / лоджий"""
            balcony: Optional[str] = None
            no: Optional[str] = None
            loggia: Optional[str] = None
            balcony_and_loggia: Optional[str] = None
            terrace: Optional[str] = None

        @dataclass
        class Bathroom:
            """Санузел"""
            separate: Optional[str] = None
            combined: Optional[str] = None
            two_or_more: Optional[str] = None

        @dataclass
        class CeilingHeight:
            """Высота потолков"""
            height_2_5: Optional[str] = None
            height_2_7: Optional[str] = None
            height_3: Optional[str] = None
            height_3_5: Optional[str] = None
            height_4: Optional[str] = None
