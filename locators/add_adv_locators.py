from enum import Enum


class AddAdvLocators(Enum):
    """Локаторы для страницы - 'Подать объявление'
    """

    URL = "https://realt.by/podat-obyavlenie/"

    SELL = '[role="button"]:has-text("Продать")'
    RESIDENTIAL = '[role="button"]:has-text("Жилая")'
    FLAT = '[role="button"]:has-text("Квартира")'
