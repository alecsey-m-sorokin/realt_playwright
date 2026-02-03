from dataclasses import dataclass

from playwright.sync_api import Page, Locator

@dataclass
class BasePageLocators:
    """Локаторы для страницы - 'Подать объявление продажа квартиры'"""

    page: Page
    wait_timeout = 5000
    common_delay = 1000

    def locate_element(self, name: str) -> Locator:
        # {name} подставится в строку при вызове метода
        role_locator = self.page.get_by_role(role="button", name=name, exact=True)
        text_locator = self.page.get_by_text(name, exact=True)
        return role_locator.or_(text_locator)

    def location_dropdown_v2(self, name: str, by_role: bool = True) -> Locator:
        if by_role:
            return self.page.get_by_role(role="button", name=name)
        return self.page.get_by_text(name, exact=True)

    def get_location_dropdown_v3(self, name: str) -> Locator:
        # Ищет элемент, который либо является кнопкой с таким текстом,
        # либо просто элементом с таким текстом (предпочтение кнопке)
        return self.page.locator(f'role=button[name="{name}"], text="{name}"').first

    def __init__(self, page: Page):
        self.page = page
        """Расположение - Location"""
        self.location_settlement = page.get_by_role(role="textbox", name="Адрес")
        # self.location_settlement_dropdown = lambda name: page.get_by_role(role="button", name=name)
        self.location_street = page.get_by_role(role="textbox", name="Улица")
        # self.location_street_dropdown = lambda name: page.get_by_role(role="button", name=name)
        self.location_house_number = page.get_by_role(role="textbox", name="Дом", exact=True)
        self.location_building_number = page.get_by_role(role="textbox", name="Корпус")
