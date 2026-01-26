from dataclasses import dataclass
from playwright.sync_api import Page, Locator

@dataclass
class LoginPageLocators:
    page: Page

    @dataclass
    class Auth:
        def __init__(self, page: Page):
            self.login_link = page.get_by_role("link", name="Войти")
            self.email_field = page.get_by_role("textbox", name="Email / логин / +")
            self.continue_button = page.get_by_role("button", name="Продолжить")
            self.password_field = page.get_by_role("textbox", name="Введите пароль")
            self.submit_button = page.get_by_role("button", name="Войти")

    @dataclass
    class Navigation:
        def __init__(self, page: Page):
            self.add_ad_button = page.get_by_role("button", name="Добавить объявление")

    @dataclass
    class AdTypeSelection:
        def __init__(self, page: Page):
            self.rent_long_term = page.get_by_role("button", name="Сдать длительно")
            self.residential = page.get_by_role("button", name="Жилая")
            self.apartment = page.get_by_role("button", name="Квартира")

    def __post_init__(self):
        self.auth = self.Auth(self.page)
        self.nav = self.Navigation(self.page)
        self.ad_selection = self.AdTypeSelection(self.page)
