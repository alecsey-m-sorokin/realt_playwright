from dataclasses import dataclass
from enum import Enum

from playwright.sync_api import Page


class AddAdvLocators(Enum):
    """Локаторы для страницы - 'Подать объявление'
    """

    URL = "https://realt.by/podat-obyavlenie/"

    SELL = '[role="button"]:has-text("Продать")'
    RESIDENTIAL = '[role="button"]:has-text("Жилая")'
    FLAT = '[role="button"]:has-text("Квартира")'

@dataclass
class AddAdvLocators:

    page: Page

    @dataclass
    class RentFlatForDayLocators:
        def __init__(self, page: Page):
            self.page = page
            self.url = "https://realt.by/podat-obyavlenie/"

            self.rent = page.get_by_role("button", name="Сдать посуточно")
            self.residential = page.get_by_role("button", name="Жилая")
            self.flat = page.get_by_role("button", name="Квартира")

