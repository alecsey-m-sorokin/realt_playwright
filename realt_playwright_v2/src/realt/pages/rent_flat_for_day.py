from __future__ import annotations

from dataclasses import dataclass

from playwright.sync_api import Page

from realt.config.settings import Settings
from realt.core.base_page import BasePage
from realt.locators.rent_flat_for_day import RentFlatForDayLocators
from realt.models.object_location import ObjectLocation
from realt.models.rent_flat_for_day import RentFlatForDayData
from realt.pages.components.area_section import AreaSection
from realt.pages.components.capacity_section import CapacitySection
from realt.pages.components.house_section import HouseSection
from realt.pages.components.location_section import LocationSection
from realt.pages.components.object_section import ObjectSection


@dataclass(frozen=True, slots=True)
class RentFlatForDayPage(BasePage):
    page: Page
    settings: Settings

    @property
    def locators(self) -> RentFlatForDayLocators:
        return RentFlatForDayLocators(page=self.page)

    def open_form(self) -> "RentFlatForDayPage":
        self.page.goto(f"{self.settings.base_url}/podat-obyavlenie/")
        self.click(self.locators.add_adv_button)
        self.click(self.locators.rent_for_day_button)
        self.click(self.locators.residential_button)
        self.click(self.locators.flat_button)
        self.click(self.locators.understand_button)
        return self

    @property
    def location(self) -> LocationSection:
        return LocationSection(page=self.page)

    @property
    def object(self) -> ObjectSection:
        return ObjectSection(page=self.page)

    @property
    def area(self) -> AreaSection:
        return AreaSection(page=self.page)

    @property
    def house(self) -> HouseSection:
        return HouseSection(page=self.page)

    @property
    def capacity(self) -> CapacitySection:
        return CapacitySection(page=self.page)

    def select_object_params(self, data: RentFlatForDayData) -> "RentFlatForDayPage":
        self.object.fill(data.object)
        return self

    def fill_area(self, data: RentFlatForDayData) -> "RentFlatForDayPage":
        self.area.fill(data.area)
        return self

    def fill_house(self, data: RentFlatForDayData) -> "RentFlatForDayPage":
        self.house.fill(data.house)
        return self

    def fill_capacity(self, data: RentFlatForDayData) -> "RentFlatForDayPage":
        self.capacity.fill(data.capacity)
        return self

    def fill_location(self, location: ObjectLocation) -> "RentFlatForDayPage":
        self.location.fill(location)
        return self
