from dataclasses import dataclass

from playwright.sync_api import Page, Locator

@dataclass
class LoginPageLocators:
    """Локаторы для страницы - авторизация'"""

    page: Page

    def __init__(self, page: Page):
        self.url = "https://realt.by/login/?nextPage=/"
        self.login_link = page.get_by_role(role="link", name="Войти")
        self.email_field = page.get_by_role(role="textbox", name="Email / логин / +")
        self.continue_button = page.get_by_role(role="button", name="Продолжить")
        self.password_field = page.get_by_role(role="textbox", name="Введите пароль")
        self.submit_button = page.get_by_role(role="button", name="Войти")
