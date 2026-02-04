from __future__ import annotations

from dataclasses import dataclass

from playwright.sync_api import Locator, Page

from realt.core.base_page import BasePage
from realt.models.rent_flat_for_day import RentFlatForDayCapacity
from realt.pages.components.containers import Containers


@dataclass(frozen=True, slots=True)
class CapacitySection(BasePage):
    page: Page

    @property
    def root(self) -> Locator:
        return self.page.locator(Containers().capacity)

    @property
    def guests_max(self) -> Locator:
        return self.root.get_by_role("textbox", name="Максимум гостей")

    def fill(self, data: RentFlatForDayCapacity) -> "CapacitySection":
        super().fill(self.guests_max, data.guests_max)
        return self
