from __future__ import annotations

from dataclasses import dataclass

from playwright.sync_api import Locator, Page


@dataclass(frozen=True, slots=True)
class RentFlatForDayLocators:
    page: Page

    @property
    def add_adv_button(self) -> Locator:
        return self.page.get_by_role("button", name="Добавить объявление")

    @property
    def rent_for_day_button(self) -> Locator:
        return self.page.get_by_role("button", name="Сдать посуточно")

    @property
    def residential_button(self) -> Locator:
        return self.page.get_by_role("button", name="Жилая")

    @property
    def flat_button(self) -> Locator:
        return self.page.get_by_role("button", name="Квартира")

    @property
    def understand_button(self) -> Locator:
        return self.page.get_by_role("button", name="Понятно")

    @property
    def location_settlement(self) -> Locator:
        return self.page.get_by_role("textbox", name="Адрес")

    @property
    def location_street(self) -> Locator:
        return self.page.get_by_role("textbox", name="Улица")

    @property
    def location_house_number(self) -> Locator:
        return self.page.get_by_role("textbox", name="Дом", exact=True)

    @property
    def location_building_number(self) -> Locator:
        return self.page.get_by_role("textbox", name="Корпус")

    @property
    def object_container(self) -> Locator:
        return self.page.locator("#object")

    def object_type(self, name: str) -> Locator:
        return self.page.get_by_text(name, exact=True)

    def object_rooms(self, rooms: str) -> Locator:
        return self.object_container.get_by_text(rooms, exact=True)

    def object_kitchen(self, name: str) -> Locator:
        return self.object_container.get_by_text(name, exact=True)

    def object_repair(self, name: str) -> Locator:
        return self.object_container.get_by_text(name, exact=True)

    @property
    def area_total(self) -> Locator:
        return self.page.get_by_role("textbox", name="Площадь общая, м²")

    @property
    def area_living(self) -> Locator:
        return self.page.get_by_role("textbox", name="Площадь жилая, м²")

    @property
    def area_kitchen(self) -> Locator:
        return self.page.get_by_role("textbox", name="Площадь кухни, м²")

    @property
    def house_floor(self) -> Locator:
        return self.page.get_by_role("textbox", name="Этаж", exact=True)

    @property
    def house_floors_total(self) -> Locator:
        return self.page.get_by_role("textbox", name="Этажей в доме")

    @property
    def house_year_built(self) -> Locator:
        return self.page.get_by_role("textbox", name="Год постройки")

    @property
    def capacity_guests_max(self) -> Locator:
        return self.page.get_by_role("textbox", name="Максимум гостей")
