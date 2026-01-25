# from locators.main_page_l import LoginPageLocators

from locators.login_page.login_page_l import LoginPageLocators
from locators.media_page.upload_photos_page_locators import UploadPhotosPageLocators
from locators.sell.residential.sell_residential_flat_locators import SellResidentialFlatLocators

from pages.login_page.login_page import LoginPage
from pages.sell.residential.sell_residential_flat_page import SellResidentialFlatPage
from pages.media_page.upload_photos_page import UploadMediaPage
from utils.functions import get_project_root


class TestLoginAndSellFlat:
    """Тесты для логина и заполнения формы продажи квартиры на realt.by
    """

    def test_successful_login_and_sell_flat(self, page):
        """Тест успешного логина и подачи объявления продажа квартиры"""

        login_page_locators = LoginPageLocators(page)
        login_page = LoginPage(page, login_page_locators)
        login_page\
            .open() \
            .is_loaded() \
            .fill_email('prod_user_01@rover.info') \
            .click_continue() \
            .wait(1000) \
            .fill_password('Oracle01') \
            .submit() \
            .wait(1000) \
            .should_be_logged_in()

        """Расположение - Location"""
        sell_residential_page_locators = SellResidentialFlatLocators(page)
        sell_page = SellResidentialFlatPage(page, sell_residential_page_locators)
        sell_page\
            .open() \
            .click_add_adv() \
            .is_loaded() \
            .click_sell_button() \
            .click_residential_button() \
            .click_flat_button() \
            .fill_settlement(location='Минск', name='г. Минск Минский р-н, Минская область') \
            .fill_street(location='Берута', name='Берута ул') \
            .fill_house_number(number='11') \
            .fill_building_number(number='а') \
            .wait(1000)

        """Квартира - Apartment """
        sell_page \
            .fill_apartment_rooms(rooms='4') \
            .fill_apartment_separate_rooms(rooms='4') \
            .fill_apartment_storey(storey='9') \
            .fill_apartment_repair(repair='Евроремонт') \
            .fill_apartment_balcony(balcony='Балкон и лоджия')

        """Площадь - Area"""
        sell_page \
            .fill_area_total(total='100') \
            .fill_area_living(living='80')

        """Дом - House"""
        sell_page \
            .fill_house_storeys('16') \
            .fill_house_building_year('2010')

        """Условия сделки - Terms Of Deal"""
        """валюта - цена - возможен торг - собственность - условия сделки """
        sell_page \
            .fill_terms_of_deal_currency(currency='USD') \
            .fill_terms_of_deal_currency_price(price='250000') \
            .fill_terms_of_deal_bargain(bargain='Возможен торг') \
            .fill_terms_of_deal_currency_ownership(ownership='Частная') \
            .fill_terms_of_deal_terms_of_deal(terms_of_deal='Чистая продажа') \
            .wait(3000)

        """Медиа - Upload Media"""
        upload_photos_page_locators = UploadPhotosPageLocators(page)
        upload_media_page = UploadMediaPage(page, upload_photos_page_locators)
        project_root = get_project_root()
        photos = [(project_root / item).as_posix() for item in upload_photos_page_locators.photos]
        upload_media_page.upload_photos(photos=photos)

        """Контакты - Contacts"""
        sell_page \
            .fill_description_short_description(short_description='Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat.') \
            .fill_contacts_phones(phones="296645311") \
            .fill_contacts_name(name="prod_user_01") \
            .click_save_and_continue() \
            .wait(3000)
