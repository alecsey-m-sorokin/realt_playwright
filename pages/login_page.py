from dataclasses import dataclass

from playwright.sync_api import Page, expect
from locators.login_page_locators import LoginPageLocators as Lpl


@dataclass
class LoginPage:
    """Page Object для страницы логина"""

    page: Page
    url: str = "https://realt.by/login/?nextPage=/"

    def open(self):
        """Открыть страницу логина"""
        self.page.goto(self.url)

    def fill_email(self, email: str):
        """Ввести email"""
        self.page.fill(Lpl.EMAIL_INPUT.value, email)

    def fill_password(self, password: str):
        """Ввести пароль"""
        self.page.fill(Lpl.PASSWORD_INPUT.value, password)

    def click_submit(self):
        """Нажать кнопку submit"""
        self.page.click(Lpl.SUBMIT_BUTTON.value)

    def login(self, email: str, password: str):
        """Выполнить логин"""
        self.fill_email(email)
        self.click_submit()
        self.fill_password(password)
        self.click_submit()

    def should_be_logged_in(self):
        """Проверить успешный логин"""
        expect(self.page).not_to_have_url(self.url)
