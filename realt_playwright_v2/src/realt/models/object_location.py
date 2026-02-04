from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ObjectLocation:
    settlement: str
    settlement_name: str
    street: str
    street_name: str
    house_number: str
    building_number: str
