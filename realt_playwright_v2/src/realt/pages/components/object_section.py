from __future__ import annotations

from dataclasses import dataclass

from playwright.sync_api import Locator, Page

from realt.core.base_page import BasePage
from realt.models.rent_flat_for_day import RentFlatForDayObject
from realt.pages.components.containers import Containers


@dataclass(frozen=True, slots=True)
class ObjectSection(BasePage):
    page: Page

    @property
    def root(self) -> Locator:
        return self.page.locator(Containers().object)

    def select_rooms(self, rooms: str) -> "ObjectSection":
        self.click(self.root.get_by_text(rooms, exact=True))
        return self

    def select_kitchen(self, kitchen: str) -> "ObjectSection":
        self.click(self.root.get_by_text(kitchen, exact=True))
        return self

    def select_repair(self, repair: str) -> "ObjectSection":
        self.click(self.root.get_by_text(repair, exact=True))
        return self

    def fill(self, data: RentFlatForDayObject) -> "ObjectSection":
        self.select_rooms(data.object_rooms)
        self.select_kitchen(data.object_kitchen)
        self.select_repair(data.object_repair)
        return self
