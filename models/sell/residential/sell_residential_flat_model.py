from dataclasses import dataclass
from typing import Optional, Any, List


@dataclass
class SellResidentialFlatModel:
    @dataclass
    class Location:
        settlement: str
        street: Optional[str] = None
        house_number: Optional[str] = None
        building_number: Optional[str] = None

    @dataclass
    class Apartment:
        rooms: int
        separate_rooms: int
        storey: int

        @dataclass
        class Repair:
            euro: Optional[str] = None
            cosmetic: Optional[str] = None
            designer: Optional[str] = None
            without: Optional[str] = None

        repair: Optional[Repair] = None

        @dataclass
        class Balcony:
            balcony: Optional[str] = None
            no: Optional[str] = None
            loggia: Optional[str] = None
            balcony_and_loggia: Optional[str] = None
            terrace: Optional[str] = None

        balcony: Optional[Balcony] = None

        @dataclass
        class Bathroom:
            separate: Optional[str] = None
            combined: Optional[str] = None
            two_or_more: Optional[str] = None

        bathroom: Optional[Bathroom] = None

        @dataclass
        class CeilingHeight:
            height_2_5: Optional[str] = None
            height_2_7: Optional[str] = None
            height_3: Optional[str] = None
            height_3_5: Optional[str] = None
            height_4: Optional[str] = None

        ceiling_height: Optional[CeilingHeight] = None

    @dataclass
    class Area:
        total: Optional[str] = None
        living: Optional[str] = None

    @dataclass
    class House:
        storeys: Optional[str] = None
        building_year: Optional[str] = None

    @dataclass
    class Additional:

        @dataclass
        class Appliance:
            phone: Optional[str] = None
            guard: Optional[str] = None
            elevator: Optional[str] = None
            internet: Optional[str] = None
            video: Optional[str] = None

        appliance: Optional[Appliance] = None

    @dataclass
    class TermsOfDeal:

        @dataclass
        class Currency:
            byn: Optional[str] = None
            usd: Optional[str] = None
            eur: Optional[str] = None

        @dataclass
        class Price:
            value: int

        @dataclass
        class Ownership:
            private: Optional[str] = None
            public: Optional[str] = None
            shared: Optional[str] = None
            bonds: Optional[str] = None

        price: Price
        currency: Optional[Currency] = None
        ownership: Optional[Ownership] = None
        bargain: Optional[bool] = False
        sale_type: Optional[str] = None

    @dataclass
    class Media:
        photos: List[str]
        photos_layout: List[str]

    @dataclass
    class Description:
        short: str
        full: str

    @dataclass
    class Contacts:
        phone: str
        name: str
        email: Optional[str] = None
        communication_pref: Optional[str] = None

    location: Location
    apartment: Apartment
    area: Optional[Area] = None
    house: Optional[House] = None
    additional: Optional[Additional] = None
    terms: Optional[TermsOfDeal] = None
    media: Optional[Media] = None
    description: Optional[Description] = None
    contacts: Optional[Contacts] = None
