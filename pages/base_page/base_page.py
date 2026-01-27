from dataclasses import dataclass
from typing import Union, Callable

from playwright.sync_api import Page, expect, Locator

from locators.base_page.base_page_locators import BasePageLocators
from locators.sell.residential.sell_residential_flat_locators import SellResidentialFlatLocators


@dataclass
class BasePage:
    """Page Object для страницы 'base_page'"""

    page: Page
    wait_timeout = 1000
    common_delay = 1000
    locators: BasePageLocators

    def __getattr__(self, name):
        # Проверяем, есть ли такой метод у объекта page
        attr = getattr(self.page, name)
        if callable(attr):
            def wrapper(*args, **kwargs):
                attr(*args, **kwargs)
                return self
            return wrapper
        return attr

    def execute(self, action: Callable[[Page], None]) -> 'BasePage':
        """Выполняет любое действие с page и возвращает self
        :param action: Действие, которое нужно выполнить
        :return: self
        :example: execute(lambda p: p.wait_for_timeout(timeout=500))
        """
        action(self.page)
        return self

    def _wait_and_fill(self, locator: Union[Locator, str], value: str, timeout: int = wait_timeout, clear: bool = True) -> None:
        """Общий метод для заполнения полей ввода"""
        element = self.page.locator(locator) if isinstance(locator, str) else locator
        element.wait_for(state="visible", timeout=timeout)
        element.scroll_into_view_if_needed()
        element.clear() if clear else None
        element.fill(str(value))
        self.page.wait_for_timeout(self.common_delay)

    def _wait_and_click(self, locator: Union[Locator, str], timeout: int = wait_timeout) -> None:
        """Общий метод для клика по элементу"""
        element = self.page.locator(locator) if isinstance(locator, str) else locator
        element.wait_for(state="visible", timeout=timeout)
        element.scroll_into_view_if_needed()
        element.click()
        self.page.wait_for_timeout(self.common_delay)

    def is_loaded(self, url: str):
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_url(url)
        self.page.wait_for_timeout(1000)
        return self

    def wait(self, timeout: float):
        self.page.wait_for_timeout(timeout)
        return self

    def open(self, url: str):
        """Открыть страницу"""
        self.page.goto(url)
        return self

    def click_add_adv(self):
        """Нажать кнопку 'Подать за 0 BYN'"""
        self.page.get_by_role(role="button", name="Добавить объявление").click()
        self.page.wait_for_timeout(1000)
        return self

    def fill_location(self):

        return self

    @property
    def location(self):
        """Позволяет обращаться к методам как page.location.fill_settlement(...)"""
        return self.Location(self)


    @dataclass
    class Location:

        base: BasePage

        def fill_settlement(self, location: str, name) -> 'base.Location':
            """Заполнить поле 'Населенный пункт, район, область'"""
            self.base._wait_and_fill(locator=self.base.locators.location_settlement, value=location)
            self.base._wait_and_click(locator=self.base.locators.location_dropdown(name))
            return self

        def fill_street(self, location: str, name) -> 'BasePage.Location':
            """Заполнить поле 'Улица'"""
            self.base._wait_and_fill(locator=self.base.locators.location_street, value=location)
            self.base._wait_and_click(locator=self.base.locators.location_dropdown(name))
            return self

        def fill_house_number(self, number: str) -> 'BasePage.Location':
            """Заполнить поле 'Дом'"""
            self.base._wait_and_fill(locator=self.base.locators.location_house_number, value=number)
            return self

        def fill_building_number(self, number: str) -> 'BasePage.Location':
            """Заполнить поле 'Корпус'"""
            self.base._wait_and_fill(locator=self.base.locators.location_building_number, value=number)
            return self

        def parent(self):
            """Метод для выхода из Location обратно в BasePage"""
            return self.base
