from __future__ import annotations

from dataclasses import dataclass

from playwright.sync_api import Locator, Page

from realt.core.base_page import BasePage
from realt.models.object_location import ObjectLocation


@dataclass(frozen=True, slots=True)
class LocationComponent(BasePage):
    page: Page

    settlement_input: Locator
    street_input: Locator
    house_input: Locator
    building_input: Locator

    def fill(self, location: ObjectLocation) -> "LocationComponent":
        super().fill(self.settlement_input, location.settlement)
        super().click(self.page.get_by_role("button", name=location.settlement_name))

        super().fill(self.street_input, location.street)
        super().click(self.page.get_by_role("button", name=location.street_name))

        super().fill(self.house_input, location.house_number)
        super().fill(self.building_input, location.building_number)
        return self
