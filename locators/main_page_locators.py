from enum import Enum


class MainPageLocators(Enum):
    """Локаторы для главной страницы - realt.by"""

    URL = "https://realt.by/"
    ADD_ADV = 'button:has-text("Подать за 0 BYN"):not(.lg\\:hidden)'
