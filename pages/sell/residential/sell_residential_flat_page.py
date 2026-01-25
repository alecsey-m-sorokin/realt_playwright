from dataclasses import dataclass
from typing import Union

from playwright.sync_api import Page, expect, Locator
from locators.sell.residential.sell_residential_flat_locators import SellResidentialFlatLocators


@dataclass
class SellResidentialFlatPage:
    """Page Object для страницы 'Подать объявление'"""

    page: Page
    locators: SellResidentialFlatLocators
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

    def open(self) -> 'LoginPage':
        """Открыть страницу подачи"""
        self.page.goto(self.locators.url)
        return self

    def click_add_adv(self) -> 'SellResidentialFlatPage':
        """Нажать кнопку 'Подать за 0 BYN'"""
        self.locators.add_adv_button.click()
        self.page.wait_for_timeout(1000)
        return self

    def is_loaded(self) -> 'SellResidentialFlatPage':
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_url(self.locators.url)
        self.page.wait_for_timeout(1000)
        return self

    def wait(self, timeout: float) -> 'SellResidentialFlatPage':
        self.page.wait_for_timeout(timeout)
        return self

    def click_sell_button(self) -> 'SellResidentialFlatPage':
        """Нажать кнопку 'Продать'"""
        self.locators.sell_button.click()
        self.page.wait_for_timeout(timeout=self.common_delay)
        return self

    def click_residential_button(self) -> 'SellResidentialFlatPage':
        """Нажать кнопку 'Жилая'"""
        self.locators.residential_button.click()
        self.page.wait_for_timeout(timeout=self.common_delay)
        return self

    def click_flat_button(self) -> 'SellResidentialFlatPage':
        """Нажать кнопку 'Квартира'"""
        self.locators.flat_button.click()
        self.page.wait_for_timeout(timeout=self.common_delay)
        return self

    def fill_settlement(self, location: str, name) -> 'SellResidentialFlatPage':
        """Заполнить поле 'Населенный пункт, район, область'"""
        self._wait_and_fill(locator=self.locators.location_settlement, value=location)
        self._wait_and_click(locator=self.locators.location_dropdown(name))
        return self

    def fill_street(self, location: str, name):
        """Заполнить поле 'Улица'"""
        self._wait_and_fill(locator=self.locators.location_street, value=location)
        self._wait_and_click(locator=self.locators.location_dropdown(name))
        return self

    def fill_house_number(self, number: str) -> 'SellResidentialFlatPage':
        """Заполнить поле 'Дом'"""
        self._wait_and_fill(locator=self.locators.location_house_number, value=number)
        return self

    def fill_building_number(self, number: str) -> 'SellResidentialFlatPage':
        """Заполнить поле 'Корпус'"""
        self._wait_and_fill(locator=self.locators.location_building_number, value=number)
        return self

    def fill_apartment_rooms(self, rooms: str) -> 'SellResidentialFlatPage':
        """Выбрать "Квартира" - 'Комнат'"""
        self._wait_and_click(locator=self.locators.location_dropdown(rooms))
        return self

    def fill_apartment_separate_rooms(self, rooms: str) -> 'SellResidentialFlatPage':
        """Выбрать "Квартира" - 'Комнат' - 'Раздельных комнат'"""
        self._wait_and_fill(locator=self.locators.apartment_separate_rooms, value=rooms)
        return self

    def fill_apartment_storey(self, storey: str) -> 'SellResidentialFlatPage':
        """Выбрать "Квартира" - 'Этаж'"""
        self._wait_and_fill(locator=self.locators.apartment_storey, value=storey)
        return self

    def fill_apartment_repair(self, repair: str) -> 'SellResidentialFlatPage':
        """Выбрать "Квартира" - 'Ремонт'"""
        self._wait_and_click(locator=self.locators.location_dropdown(repair))
        return self

    def fill_apartment_balcony(self, balcony: str) -> 'SellResidentialFlatPage':
        """Выбрать "Квартира" - 'Балконов / лоджий'"""
        self._wait_and_click(locator=self.locators.location_dropdown(balcony))
        return self

    def fill_area_total(self, total: str) -> 'SellResidentialFlatPage':
        """Заполнить поле 'Площадь - Площадь общая, м²'"""
        self._wait_and_fill(locator=self.locators.area_total, value=total)
        return self

    def fill_area_living(self, living: str) -> 'SellResidentialFlatPage':
        """Заполнить поле 'Площадь - Площадь жилая, м²'"""
        self._wait_and_fill(locator=self.locators.area_living, value=living)
        return self

    def fill_house_storeys(self, storeys: str) -> 'SellResidentialFlatPage':
        """Заполнить поле 'Дом - Этажей в доме'"""
        self._wait_and_fill(locator=self.locators.house_storeys, value=storeys)
        return self

    def fill_house_building_year(self, year: str) -> 'SellResidentialFlatPage':
        """Заполнить поле 'Дом - Год постройки'"""
        self._wait_and_fill(locator=self.locators.house_building_year, value=year)
        return self

    def fill_terms_of_deal_currency(self, currency: str) -> 'SellResidentialFlatPage':
        """Выбрать "Условия сделки" - 'Цена - Валюта'"""
        self._wait_and_click(locator=self.locators.location_dropdown(currency))
        return self

    def fill_terms_of_deal_currency_price(self, price: str) -> 'SellResidentialFlatPage':
        """Выбрать "Условия сделки" - 'Цена'"""
        self._wait_and_fill(locator=self.locators.terms_of_deal_price, value=price)
        return self

    def fill_terms_of_deal_bargain(self, bargain: str) -> 'SellResidentialFlatPage':
        """Выбрать "Условия сделки" - 'Возможен торг'"""
        self.page.get_by_text(text='Возможен торг').click()
        # self._wait_and_click(locator=self.locators.location_dropdown(bargain))
        return self

    def fill_terms_of_deal_currency_ownership(self, ownership: str) -> 'SellResidentialFlatPage':
        """Выбрать "Условия сделки" - 'Собственность'"""
        self._wait_and_click(locator=self.locators.location_dropdown(ownership))
        return self

    def fill_terms_of_deal_terms_of_deal(self, terms_of_deal: str) -> 'SellResidentialFlatPage':
        """Выбрать "Условия сделки" - 'Условия сделки'"""
        self._wait_and_click(locator=self.locators.location_dropdown(terms_of_deal))
        return self

    def fill_description_short_description(self, short_description: str) -> 'SellResidentialFlatPage':
        """Заполнить поле "Описание" - 'Краткое описание'"""
        self._wait_and_fill(locator=self.locators.description_short_description, value=short_description)
        return self

    def fill_contacts_phones(self, phones: str) -> 'SellResidentialFlatPage':
        """Заполнить поле "Контакты" - 'Телефон'"""
        self._wait_and_click(locator=self.locators.contacts_show_phones_list)
        self._wait_and_click(locator=self.locators.contacts_clear_phone)
        self._wait_and_fill(locator=self.locators.contacts_phone, value=phones, clear=False)
        return self

    def fill_contacts_name(self, name: str) -> 'SellResidentialFlatPage':
        """Заполнить поле "Контакты" - 'Имя (контактное)'"""
        self._wait_and_fill(locator=self.locators.contacts_name, value=name)
        return self

    def click_save_and_continue(self) -> 'SellResidentialFlatPage':
        """Нажать 'Сохранить и продолжить'"""
        self._wait_and_click(locator=self.locators.save_and_continue)
        return self
