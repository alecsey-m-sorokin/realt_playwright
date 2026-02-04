from dataclasses import dataclass

from playwright.sync_api import Page, Locator

@dataclass
class BasePageLocators:
    """базовые локаторы"""

    page: Page
    wait_timeout = 5000
    common_delay = 1000

    def __init__(self, page: Page):
        self.page = page
        """Расположение - Location"""
        self.location_settlement = page.get_by_role(role="textbox", name="Адрес")
        self.location_street = page.get_by_role(role="textbox", name="Улица")
        self.location_house_number = page.get_by_role(role="textbox", name="Дом", exact=True)
        self.location_building_number = page.get_by_role(role="textbox", name="Корпус")
