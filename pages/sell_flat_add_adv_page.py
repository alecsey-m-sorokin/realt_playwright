from dataclasses import dataclass
from typing import Optional

from loguru import logger
from playwright.sync_api import Page, expect
from locators.add_adv_locators import AddAdvLocators as AddAL
from locators.sell_flat_add_adv_locators import SellFlatAddAdvLocators as SellFlatAddAdvL

@dataclass
class SellFlatAddAdvPage:
    """Page Object для страницы 'Подать объявление - продажа квартира'"""
    page: Page
    wait_timeout = 5000
    common_delay = 1000

    def _wait_and_fill(self, locator: str, value: str, timeout: int = wait_timeout, clear: bool = True) -> None:
        """Общий метод для заполнения полей ввода"""
        element = self.page.locator(locator)
        element.wait_for(state="visible", timeout=timeout)
        element.scroll_into_view_if_needed()
        element.clear() if clear else None
        element.fill(str(value))
        self.page.wait_for_timeout(self.common_delay)

    def _wait_and_click(self, locator: str, timeout: int = wait_timeout) -> None:
        """Общий метод для клика по элементу"""
        element = self.page.locator(locator)
        element.wait_for(state="visible", timeout=timeout)
        element.scroll_into_view_if_needed()
        element.click()
        self.page.wait_for_timeout(self.common_delay)

    def _select_dropdown(self, location: str) -> None:
        """Общий метод для выбора опции из выпадающего списка"""
        element = self.page.locator(SellFlatAddAdvL.LOCATION_DROPDOWN.value).filter(has_text=location).first
        element.wait_for(state="visible", timeout=6000)
        element.click(delay=100)

    def is_loaded(self):
        """Проверяет, что страница полностью загружена и основные элементы видны"""
        self.page.wait_for_load_state("load")
        expect(self.page, "URL страницы не совпадает с ожидаемым").to_have_url(SellFlatAddAdvL.URL.value)
        expect(self.page.locator(SellFlatAddAdvL.CONTAINER.value), "Элемент контейнера не отобразился на странице").to_be_visible(timeout=10000)

    def fill_settlement(self, location: str):
        """Заполнить поле 'Населенный пункт, район, область'"""
        self._wait_and_fill(locator=SellFlatAddAdvL.LOCATION_SETTLEMENT.value, value=location)
        self._select_dropdown(location=location)

    def fill_street(self, location: str):
        """Заполнить поле 'Улица'"""
        self._wait_and_fill(locator=SellFlatAddAdvL.LOCATION_STREET.value, value=location)
        self._select_dropdown(location=location)

    def fill_house_number(self, number: str):
        """Заполнить поле 'Дом'"""
        self._wait_and_fill(locator=SellFlatAddAdvL.HOUSE_NUMBER.value, value=number)

    def fill_building_number(self, number: str):
        """Заполнить поле 'Корпус'"""
        self._wait_and_fill(locator=SellFlatAddAdvL.BUILDING_NUMBER.value, value=number)

    def fill_apartment_rooms(self, rooms: str):
        """Выбрать "Квартира" - 'Комнат'"""
        locator = SellFlatAddAdvL.APARTMENT_ROOMS.value.format(rooms=rooms)
        self._wait_and_click(locator=locator)

    def fill_apartment_separate_rooms(self, rooms: str):
        """Выбрать "Квартира" - 'Комнат' - 'Раздельных комнат'"""
        self._wait_and_fill(locator=SellFlatAddAdvL.SEPARATE_ROOMS.value, value=rooms)

    def fill_apartment_storey(self, storey: str):
        """Выбрать "Квартира" - 'Этаж'"""
        self._wait_and_fill(locator=SellFlatAddAdvL.APARTMENT_STOREY.value, value=storey)

    def fill_apartment_balcony(self, balcony: str):
        """Выбрать "Квартира" - 'Балконов / лоджий'"""
        locator = SellFlatAddAdvL.APARTMENT_BALCONY.value.format(balcony=balcony)
        self._wait_and_click(locator=locator)

    def fill_area_total(self, total: str):
        """Заполнить поле 'Площадь - Площадь общая, м²'"""
        self._wait_and_fill(locator=SellFlatAddAdvL.AREA_TOTAL.value, value=total)

    def fill_area_living(self, living: str):
        """Заполнить поле 'Площадь - Площадь жилая, м²'"""
        self._wait_and_fill(locator=SellFlatAddAdvL.AREA_LIVING.value, value=living)

    def fill_house_storeys(self, storeys: str):
        """Заполнить поле 'Дом - Этажей в доме'"""
        self._wait_and_fill(locator=SellFlatAddAdvL.HOUSE_STOREYS.value, value=storeys)

    def fill_house__building_year(self, year: str):
        """Заполнить поле 'Дом - Год постройки'"""
        self._wait_and_fill(locator=SellFlatAddAdvL.HOUSE_BUILDING_YEAR.value, value=year)

    def fill_terms_of_deal_currency(self, currency: str):
        """Выбрать "Условия сделки" - 'Цена - Валюта'"""
        locator = SellFlatAddAdvL.CURRENCY.value.format(currency=currency)
        self._wait_and_click(locator=locator)

    def fill_terms_of_deal_currency_price(self, price: str):
        """Выбрать "Условия сделки" - 'Цена'"""
        self._wait_and_fill(locator=SellFlatAddAdvL.PRICE.value, value=price)

    def fill_terms_of_deal_currency_ownership(self, ownership: str):
        """Выбрать "Условия сделки" - 'Собственность'"""
        locator = SellFlatAddAdvL.OWNERSHIP.value.format(ownership=ownership)
        self._wait_and_click(locator=locator)

    def fill_terms_of_deal_terms_of_deal(self, terms_of_deal: str):
        """Выбрать "Условия сделки" - 'Собственность'"""
        locator = SellFlatAddAdvL.TERMS_OF_DEAL.value.format(terms_of_deal=terms_of_deal)
        self._wait_and_click(locator=locator)

    def fill_description_short_description(self, short_description: str):
        """Заполнить поле "Описание" - 'Краткое описание'"""
        self._wait_and_fill(locator=SellFlatAddAdvL.SHORT_DESCRIPTION.value, value=short_description)

    def fill_contacts_phones(self, phones: str):
        """Заполнить поле "Контакты" - 'Телефон'"""
        self._wait_and_fill(locator=SellFlatAddAdvL.PHONES.value, value=phones, clear=False)

    def fill_contacts_name(self, name: str):
        """Заполнить поле "Контакты" - 'Имя (контактное)'"""
        self._wait_and_fill(locator=SellFlatAddAdvL.CONTACTS_NAME.value, value=name)

    def click_save_and_continue(self):
        """Нажать 'Сохранить и продолжить'"""
        locator = SellFlatAddAdvL.SAVE_AND_CONTINUE.value
        self._wait_and_click(locator=locator)
