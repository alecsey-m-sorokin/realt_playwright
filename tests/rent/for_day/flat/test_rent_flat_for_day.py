from dataclasses import asdict

from locators.login_page.login_page_locators import LoginPageLocators
from locators.rent.for_day.flat.rent_flat_for_day_locators import RentFlatForDayLocators
from pages.login_page.login_page import LoginPage
from pages.rent.for_day.flat.rent_flat_for_day_page import RentFlatForDayPage
from test_data.login.login_test_data import Users
from test_data.object_location_test_data import ObjectLocationsTestData


class TestRentFlatForDay:
    """Тесты для логина и заполнения формы продажи квартиры на realt.by
    """

    def test_successful_login_and_rent_flat_for_day(self, page):
        """Тест успешного логина и подачи объявления аренда квартиры суточная"""
        login_page_locators = LoginPageLocators(page)
        login_page = LoginPage(page, login_page_locators)
        login_page \
            .login(Users.VALID_USER)

        """Расположение - Location"""
        rent_flat_for_day_locators = RentFlatForDayLocators(page)
        rent_page = RentFlatForDayPage(page, rent_flat_for_day_locators)
        rent_page \
            .select_adv_type() \
        .location \
            .fill_location(object_location=ObjectLocationsTestData.MINSK_BERUTA_11_A)


            # .parent() \
            # .fill_apartment_rooms(rooms='7')
