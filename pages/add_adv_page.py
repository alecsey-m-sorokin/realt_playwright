from dataclasses import dataclass

from playwright.sync_api import Page, expect
from locators.add_adv_locators import AddAdvLocators as AddAL


@dataclass
class AddAdvPage:
    """Page Object для страницы 'Подать объявление'"""

    page: Page
    url = "https://realt.by/podat-obyavlenie/"

    def is_loaded(self):
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_url(AddAL.URL.value)
        self.page.wait_for_timeout(1000)

    def click_sell_button(self):
        """Нажать кнопку 'Продать'"""
        self.page.click(AddAL.SELL.value)
        self.page.wait_for_timeout(1000)

        """Нажать кнопку 'Жилая'"""
        self.page.click(AddAL.RESIDENTIAL.value)
        self.page.wait_for_timeout(1000)

        """Нажать кнопку 'Квартира'"""
        self.page.click(AddAL.FLAT.value)
        self.page.wait_for_timeout(1000)
