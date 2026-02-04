from __future__ import annotations

from dataclasses import dataclass

from playwright.sync_api import Locator, Page

from realt.core.base_page import BasePage
from realt.models.object_location import ObjectLocation
from realt.pages.components.containers import Containers


@dataclass(frozen=True, slots=True)
class LocationSection(BasePage):
    page: Page

    @property
    def root(self) -> Locator:
        return self.page.locator(Containers().location)

    @property
    def settlement(self) -> Locator:
        return self.root.get_by_role("textbox", name="Адрес")

    @property
    def street(self) -> Locator:
        return self.root.get_by_role("textbox", name="Улица")

    @property
    def house_number(self) -> Locator:
        return self.root.get_by_role("textbox", name="Дом", exact=True)

    @property
    def building_number(self) -> Locator:
        return self.root.get_by_role("textbox", name="Корпус")

    def fill(self, location: ObjectLocation) -> "LocationSection":
        super().fill(self.settlement, location.settlement)
        super().click(self.page.get_by_role("button", name=location.settlement_name))

        super().fill(self.street, location.street)
        super().click(self.page.get_by_role("button", name=location.street_name))

        super().fill(self.house_number, location.house_number)
        super().fill(self.building_number, location.building_number)
        return self
