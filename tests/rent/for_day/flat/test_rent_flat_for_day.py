from dataclasses import asdict

from locators.login_page.login_page_locators import LoginPageLocators
from locators.rent.for_day.flat.rent_flat_for_day_locators import RentFlatForDayLocators
from pages.login_page.login_page import LoginPage
from pages.rent.for_day.flat.rent_flat_for_day_page import RentFlatForDayPage
from test_data.login.login_test_data import Users


class TestRentFlatForDay:
    """Тесты для логина и заполнения формы продажи квартиры на realt.by
    """

    def test_successful_login_and_rent_flat_for_day(self, page):
        """Тест успешного логина и подачи объявления продажа квартиры"""
        login_page_locators = LoginPageLocators(page)
        login_page = LoginPage(page, login_page_locators)
        login_page \
            .login(Users.VALID_USER)

        """Расположение - Location"""
        rent_flat_for_day_locators = RentFlatForDayLocators(page)
        rent_page = RentFlatForDayPage(page, rent_flat_for_day_locators)
        rent_page\
            .open(url=rent_flat_for_day_locators.url) \
            .click_add_adv() \
            .is_loaded(url=rent_flat_for_day_locators.url) \
            .click_rent_for_day_button() \
            .execute(lambda p: p.wait_for_timeout(timeout=500)) \
            .click_residential_button() \
            .wait_for_timeout(1000) \
            .click_flat_button() \
            .click_understand() \
            .location \
                .fill_settlement(location='Минск', name='г. Минск Минский р-н, Минская область') \
                .fill_street(location='Берута', name='Берута ул') \
                .fill_house_number(number="11") \
                .fill_building_number(number="a") \
            .parent() \
            .fill_apartment_rooms(rooms='4')

