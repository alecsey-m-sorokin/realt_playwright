from __future__ import annotations

from dataclasses import dataclass

from playwright.sync_api import Locator, Page

from realt.core.base_page import BasePage
from realt.models.rent_flat_for_day import RentFlatForDayHouse
from realt.pages.components.containers import Containers


@dataclass(frozen=True, slots=True)
class HouseSection(BasePage):
    page: Page

    @property
    def root(self) -> Locator:
        return self.page.locator(Containers().house)

    @property
    def floor(self) -> Locator:
        return self.root.get_by_role("textbox", name="Этаж", exact=True)

    @property
    def floors_total(self) -> Locator:
        return self.root.get_by_role("textbox", name="Этажей в доме")

    @property
    def year_built(self) -> Locator:
        return self.root.get_by_role("textbox", name="Год постройки")

    def fill(self, data: RentFlatForDayHouse) -> "HouseSection":
        super().fill(self.floor, data.floor)
        super().fill(self.floors_total, data.floors_total)
        super().fill(self.year_built, data.year_built)
        return self
