from dataclasses import dataclass
from typing import Union

from playwright.sync_api import Page, expect, Locator

from models.rent.for_day.flat.rent_flat_for_day_model import RentFlatForDayModel
from pages.base_page.base_page import BasePage
from locators.rent.for_day.flat.rent_flat_for_day_locators import RentFlatForDayLocators


@dataclass
class RentFlatForDayPage(BasePage):
    """Page Object для страницы 'Подать объявление аренда квартиры суточная'"""

    page: Page
    locators: RentFlatForDayLocators

    def click_rent_for_day_button(self) -> 'RentFlatForDayPage':
        """Нажать кнопку 'Сдать посуточно'"""
        self.locators.rent_flat_for_day_button.click()
        self.page.wait_for_timeout(timeout=self.common_delay)
        return self

    def click_residential_button(self) -> 'RentFlatForDayPage':
        """Нажать кнопку 'Жилая'"""
        self.locators.residential_button.click()
        self.page.wait_for_timeout(timeout=self.common_delay)
        return self

    def click_flat_button(self) -> 'RentFlatForDayPage':
        """Нажать кнопку 'Квартира'"""
        self.locators.flat_button.click()
        self.page.wait_for_timeout(timeout=self.common_delay)
        return self

    def click_understand(self) -> 'RentFlatForDayPage':
        """Нажать кнопку 'Понятно'"""
        self.page.get_by_role("button", name="Понятно").click()
        self.page.wait_for_timeout(timeout=self.common_delay)
        return self

    def select_adv_type(self):
        self.open(url=self.locators.url) \
            .click_add_adv() \
            .is_loaded(url=self.locators.url) \
            .click_rent_for_day_button() \
            .wait(500) \
            .click_residential_button() \
            .wait_for_timeout(500) \
            .click_flat_button() \
            .click_understand()
        return self

    def click_object_type(self, object_type: str) -> 'RentFlatForDayPage':
        """Выбрать "Объект" - 'Тип объекта'"""
        # self._wait_and_click(locator=self.locators.rooms)
        # self._wait_and_click(locator=self.locators.location_dropdown_v2(name=rooms, by_role=False))
        self._wait_and_click(locator=self.locators.location_dropdown(name=object_type))
        return self

    def click_object_rooms(self, object_rooms: str) -> 'RentFlatForDayPage':
        """Выбрать "Объект" - 'Комнат'"""
        # self._wait_and_click(locator=self.locators.rooms)
        # self._wait_and_click(locator=self.locators.location_dropdown_v2(name=rooms, by_role=False))

        # self._wait_and_click(locator=self.locators.location_dropdown(name=object_rooms))
        self.execute(lambda rooms: rooms.locator("#object").get_by_text(text=object_rooms, exact=True).click())
        return self

    def click_object_kitchen(self, object_kitchen: str) -> 'RentFlatForDayPage':
        """Выбрать "Объект" - 'Кухня'"""
        # self._wait_and_click(locator=self.locators.rooms)
        # self._wait_and_click(locator=self.locators.location_dropdown_v2(name=rooms, by_role=False))
        self._wait_and_click(locator=self.locators.location_dropdown(name=object_kitchen))
        return self

    def click_object_repair(self, object_repair: str) -> 'RentFlatForDayPage':
        """Выбрать "Объект" - 'Ремонт'"""
        # self._wait_and_click(locator=self.locators.rooms)
        # self._wait_and_click(locator=self.locators.location_dropdown_v2(name=rooms, by_role=False))
        self._wait_and_click(locator=self.locators.location_dropdown(name=object_repair))
        return self

    def select_object_params(self, params:  RentFlatForDayModel) -> 'RentFlatForDayPage':
        self \
            .click_object_rooms(object_rooms=params.object.object_rooms) \
            .click_object_kitchen(object_kitchen=params.object.object_kitchen) \
            .click_object_repair(object_repair=params.object.object_repair) \
            .wait(3000)
        return self

