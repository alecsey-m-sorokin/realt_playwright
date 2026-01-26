from dataclasses import dataclass
from typing import Union

from playwright.sync_api import Page, expect, Locator
from locators.sell.residential.sell_residential_flat_locators import SellResidentialFlatLocators


@dataclass
class BasePage:
    """Page Object для страницы 'base_page'"""

    page: Page
    wait_timeout = 1000
    common_delay = 1000

    def __getattr__(self, name):
        # Проверяем, есть ли такой метод у объекта page
        attr = getattr(self.page, name)
        if callable(attr):
            def wrapper(*args, **kwargs):
                attr(*args, **kwargs)
                return self  # Возвращаем SellResidentialFlatPage вместо None
            return wrapper
        return attr

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
