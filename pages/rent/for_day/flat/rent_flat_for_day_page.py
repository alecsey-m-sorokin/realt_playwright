from dataclasses import dataclass
from typing import Union

from playwright.sync_api import Page, expect, Locator
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

    def fill_apartment_rooms(self, rooms: str) -> 'RentFlatForDayPage':
        """Выбрать "Квартира" - 'Комнат'"""
        # self._wait_and_click(locator=self.locators.rooms)
        self._wait_and_click(locator=self.locators.rooms)
        return self
