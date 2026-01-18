# Pages
from pages.add_adv_page import AddAdvPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

# User data
from data.users import User
from pages.sell_flat_add_adv_page import SellFlatAddAdvPage
from pages.upload_photos_page import UploadMediaPage


class TestLogin:
    """Тесты для логина на realt.by
    """

    def test_successful_login(self, page):
        """Тест успешного логина и подачи объявления продажа квартиры"""

        login_page = LoginPage(page)
        main_page = MainPage(page)
        add_adv_page = AddAdvPage(page)
        sell_flat_add_adv_page = SellFlatAddAdvPage(page)
        upload_media_page = UploadMediaPage(page)

        login_page.open()
        login_page.login(email=User.VALID.email, password=User.VALID.password)

        main_page.is_loaded()
        main_page.click_add_adv()

        add_adv_page.is_loaded()
        add_adv_page.click_sell_button()

        sell_flat_add_adv_page.is_loaded()
        sell_flat_add_adv_page.fill_settlement(location="Минск")
        sell_flat_add_adv_page.fill_street(location="Берута")
        sell_flat_add_adv_page.fill_house_number(number="11")
        sell_flat_add_adv_page.fill_building_number(number="A")

        sell_flat_add_adv_page.fill_apartment_rooms(rooms="4")
        sell_flat_add_adv_page.fill_apartment_separate_rooms(rooms="4")
        sell_flat_add_adv_page.fill_apartment_storey(storey="9")
        sell_flat_add_adv_page.fill_apartment_balcony(balcony="Балкон и лоджия")
        #
        sell_flat_add_adv_page.fill_area_total(total="140")
        sell_flat_add_adv_page.fill_area_living(living="80")
        sell_flat_add_adv_page.fill_house_storeys(storeys="16")
        sell_flat_add_adv_page.fill_house__building_year(year="2010")
        #
        sell_flat_add_adv_page.fill_terms_of_deal_currency(currency="USD")
        sell_flat_add_adv_page.fill_terms_of_deal_currency_price(price="250000")
        sell_flat_add_adv_page.fill_terms_of_deal_currency_ownership(ownership="Частная")
        sell_flat_add_adv_page.fill_terms_of_deal_terms_of_deal(terms_of_deal="Чистая продажа")

        upload_media_page.upload_photos()

        sell_flat_add_adv_page.fill_description_short_description(short_description="Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat.")
        sell_flat_add_adv_page.fill_contacts_phones(phones="296645311")
        sell_flat_add_adv_page.fill_contacts_name(name="prod_user_01")
        sell_flat_add_adv_page.click_save_and_continue()












    #
    # def test_wrong_password(self, page):
    #     """Тест логина с неверным паролем"""
    #     login = LoginPage(page)
    #     login.open()
    #     login.login(
    #         TestUser.WRONG_PASSWORD.email,
    #         TestUser.WRONG_PASSWORD.password
    #     )
    #     login.should_see_error_message("неверный|invalid|пароль|password|ошибка")
    #
    # def test_wrong_email(self, page):
    #     """Тест логина с неверным email"""
    #     login = LoginPage(page)
    #     login.open()
    #     login.login(
    #         TestUser.WRONG_EMAIL.email,
    #         TestUser.WRONG_EMAIL.password
    #     )
    #     login.should_see_error_message("не найден|invalid|пользователь|user|ошибка")
    #
    # def test_empty_fields(self, page):
    #     """Тест логина с пустыми полями"""
    #     login = LoginPage(page)
    #     login.open()
    #     login.click_submit()  # Без ввода данных
    #     login.should_see_error_message("обязательн|required|пуст|empty|введите")
