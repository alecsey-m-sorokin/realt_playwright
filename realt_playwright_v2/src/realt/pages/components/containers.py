from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Containers:
    location: str = "#location"
    object: str = "#object"
    area: str = "#area"
    house: str = "#house"
    capacity: str = "#capacity"
    bathroom: str = "#bathroom"
    rules: str = "#rules"
    media: str = "#media"
    description: str = "#description"
    contacts: str = "#contacts"
