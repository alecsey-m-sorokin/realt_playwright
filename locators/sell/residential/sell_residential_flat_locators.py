from dataclasses import dataclass

from playwright.sync_api import Page, Locator

@dataclass
class SellResidentialFlatLocators:
    """Локаторы для страницы - 'Подать объявление продажа квартиры'"""

    page: Page
    wait_timeout = 5000
    common_delay = 1000

    def location_dropdown(self, name: str) -> Locator:
        # {name} подставится в строку при вызове метода
        return self.page.get_by_role(role="button", name=name)

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://realt.by/podat-obyavlenie/"
        self.add_adv_button = page.get_by_role(role="button", name="Добавить объявление")
        self.sell_button = page.get_by_role(role="button", name="Продать")
        self.residential_button = page.get_by_role(role="button", name="Жилая")
        self.flat_button = page.get_by_role(role="button", name="Квартира")

        """Расположение - Location"""
        self.location_settlement = page.get_by_role(role="textbox", name="Адрес")
        # self.location_settlement_dropdown = lambda name: page.get_by_role(role="button", name=name)
        self.location_street = page.get_by_role(role="textbox", name="Улица")
        # self.location_street_dropdown = lambda name: page.get_by_role(role="button", name=name)
        self.location_house_number = page.get_by_role(role="textbox", name="Дом", exact=True)
        self.location_building_number = page.get_by_role(role="textbox", name="Корпус")

        """Квартира - Apartment """
        self.apartment_rooms = page.get_by_role(role="textbox", name="4")
        self.apartment_separate_rooms = page.get_by_role(role="textbox", name="Раздельных комнат")
        self.apartment_storey = page.get_by_role(role="textbox", name="Этаж", exact=True)
        self.apartment_repair = page.get_by_role(role="button", name="Евроремонт")
        self.apartment_balcony = page.get_by_role(role="button", name="Балкон и лоджия")

        """Площадь - Area"""
        self.area_total = page.get_by_role(role="textbox", name="Площадь общая, м²")
        self.area_living = page.get_by_role(role="textbox", name="Площадь жилая, м²")

        """Дом - House"""
        self.house_storeys = page.get_by_role("textbox", name="Этажей в доме", exact=True)
        self.house_building_year = page.get_by_role("textbox", name="Год постройки")
        self.house_state = page.get_by_role("button", name="Сдан", exact=True)

        """Условия сделки - Currency"""
        self.terms_of_deal_currency = page.get_by_role("button", name="USD")
        self.terms_of_deal_price = page.get_by_role("textbox", name="Например: 50000")
        self.terms_of_deal_bargain = page.get_by_role("button", name="Возможен торг")
        self.terms_of_deal_ownership = page.get_by_role("button", name="Частная")
        self.terms_of_deal_terms_of_deal = page.get_by_role("button", name="Чистая продажа")





"""
def test_example(page: Page) -> None:
    page.goto("https://realt.by/podat-obyavlenie/")
    page.get_by_role("button", name="Принять").click()
    page.get_by_role("button", name="Продать").click()
    page.get_by_role("button", name="Жилая").click()
    page.get_by_role("button", name="Жилая").click()
    page.get_by_role("button", name="Жилая").click()
    page.get_by_role("button", name="Квартира").click()
    page.get_by_role("textbox", name="Адрес").click()
    page.get_by_role("textbox", name="Адрес").fill("Минск")
    page.get_by_role("button", name="г. Минск Минский р-н, Минская область").click()
    page.get_by_role("textbox", name="Улица").click()
    page.get_by_role("textbox", name="Улица").fill("Берута")
    page.get_by_role("button", name="Берута ул").click()
    page.get_by_role("textbox", name="Дом", exact=True).click()
    page.get_by_role("textbox", name="Дом", exact=True).fill("11")
    page.get_by_role("textbox", name="Корпус").click()
    page.get_by_role("textbox", name="Корпус").fill("а")
    page.get_by_role("button", name="4").click()
    page.get_by_role("textbox", name="Раздельных комнат").click()
    page.get_by_role("textbox", name="Раздельных комнат").fill("4")
    page.get_by_role("textbox", name="Этаж", exact=True).click()
    page.get_by_role("textbox", name="Этаж", exact=True).fill("9")
    page.get_by_role("button", name="Евроремонт").click()
    page.get_by_role("button", name="Балкон и лоджия").click()
    page.get_by_role("textbox", name="Площадь общая, м²").click()
    page.get_by_role("textbox", name="Площадь общая, м²").fill("138")
    page.get_by_role("textbox", name="Площадь жилая, м²").click()
    page.get_by_role("textbox", name="Площадь жилая, м²").fill("80")
    page.get_by_role("textbox", name="Этажей в доме").click()
    page.get_by_role("textbox", name="Этажей в доме").fill("16")
    page.get_by_role("textbox", name="Год постройки").click()
    page.get_by_role("textbox", name="Год постройки").fill("2010")
    page.get_by_role("button", name="Сдан", exact=True).click()
    page.get_by_role("textbox", name="Удобства").click()
    page.locator(".inline-block.w-5").first.click()
    page.locator("li:nth-child(2) > .font-normal.cursor-pointer > .inline-block").click()
    page.locator("li:nth-child(3) > .font-normal.cursor-pointer > .inline-block").click()
    page.locator("li:nth-child(4) > .font-normal.cursor-pointer > .inline-block").click()
    page.locator("li:nth-child(5) > .font-normal.cursor-pointer > .inline-block").click()
    page.locator("li:nth-child(6) > .font-normal.cursor-pointer > .inline-block").click()
    page.locator("li:nth-child(7) > .font-normal.cursor-pointer > .inline-block").click()
    page.get_by_role("button", name="Применить").click()
    page.get_by_role("button", name="Грузовые лифты").click()
    page.get_by_role("button", name="Выделенные места на парковке").click()
    page.get_by_role("button", name="Подземный (встроенный)").click()
    page.get_by_role("button", name="Во дворе").click()
    page.get_by_role("button", name="Открытая").click()
    page.get_by_role("button", name="USD").click()
    page.get_by_role("textbox", name="Например:").click()
    page.get_by_role("textbox", name="Например:").fill("250000")
    page.get_by_text("Возможен торг").click()
    page.get_by_role("button", name="Частная").click()
    page.get_by_role("button", name="Чистая продажа").click()
    page.get_by_role("switch", name="Конкурс / Аукцион").click()
    page.get_by_role("button", name="Выберите фотографии").click()
    page.get_by_role("button", name="Выберите фотографии").set_input_files(["026.jpg", "027.jpg", "028.jpg"])
    page.get_by_role("textbox", name="Краткое описание").click()
    page.get_by_role("textbox", name="Краткое описание").fill("краткое описание краткое описание краткое описание")
    page.get_by_role("link", name="Контакты", exact=True).click()
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("textbox", name="Email / логин / +").click()
    page.get_by_role("textbox", name="Email / логин / +").fill("dev_user_01@rover.info")
    page.get_by_role("button", name="Продолжить").click()
    page.goto("https://realt.by/login/?nextPage=%2Fpodat-obyavlenie%3FrestoreForm%3D")
    page.get_by_role("textbox", name="Email / логин / +").click()
    page.get_by_role("textbox", name="Email / логин / +").fill("prod_user_01@rover.info")
    page.get_by_role("button", name="Продолжить").click()
    page.get_by_role("textbox", name="Введите пароль").fill("Oracle01")
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("textbox", name="Телефон").click()
    page.get_by_role("textbox", name="Телефон").press("ArrowRight")
    page.get_by_role("textbox", name="Телефон").press("ArrowRight")
    page.get_by_role("textbox", name="Телефон").press("ArrowRight")
    page.get_by_role("textbox", name="Телефон").press("ArrowRight")
    page.get_by_role("textbox", name="Телефон").press("ArrowRight")
    page.get_by_role("textbox", name="Телефон").press("ArrowRight")
    page.get_by_role("textbox", name="Телефон").fill("+375(29)664-53-11_")
    page.get_by_role("textbox", name="Имя (контактное)").click()
    page.get_by_role("textbox", name="Имя (контактное)").press("End")
    page.get_by_role("textbox", name="Имя (контактное)").press("Shift+Home")
    page.get_by_role("textbox", name="Имя (контактное)").press("ControlOrMeta+c")
    page.get_by_role("textbox", name="Имя (контактное)").fill("prod_user_01@rover.info")
    page.get_by_role("button", name="Звонки", exact=True).click()
    page.get_by_role("button", name="Сохранить и продолжить").click()
    page.get_by_text("Обычное").click()

"""