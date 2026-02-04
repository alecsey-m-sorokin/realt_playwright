from __future__ import annotations

from dataclasses import dataclass

from playwright.sync_api import Locator, Page

from realt.core.base_page import BasePage
from realt.models.rent_flat_for_day import RentFlatForDayArea
from realt.pages.components.containers import Containers


@dataclass(frozen=True, slots=True)
class AreaSection(BasePage):
    page: Page

    @property
    def root(self) -> Locator:
        return self.page.locator(Containers().area)

    @property
    def total(self) -> Locator:
        return self.root.get_by_role("textbox", name="Площадь общая, м²")

    @property
    def living(self) -> Locator:
        return self.root.get_by_role("textbox", name="Площадь жилая, м²")

    @property
    def kitchen(self) -> Locator:
        return self.root.get_by_role("textbox", name="Площадь кухни, м²")

    def fill(self, data: RentFlatForDayArea) -> "AreaSection":
        super().fill(self.total, data.area_total)
        super().fill(self.living, data.area_living)
        super().fill(self.kitchen, data.area_kitchen)
        return self
