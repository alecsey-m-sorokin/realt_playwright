from dataclasses import dataclass

from loguru import logger
from playwright.sync_api import Page, expect

from locators.login_page.login_page_locators import LoginPageLocators


@dataclass
class LoginPage:

    page: Page
    locators: LoginPageLocators

    def __getattr__(self, name):
        # Проверяем, есть ли такой метод у объекта page
        attr = getattr(self.page, name)
        if callable(attr):
            def wrapper(*args, **kwargs):
                attr(*args, **kwargs)
                return self  # Возвращаем LoginPage вместо None
            return wrapper
        return attr

    @property
    def and_(self) -> 'LoginPage':
        return self

    def open(self) -> 'LoginPage':
        """Открыть страницу логина"""
        self.page.goto(self.locators.url)
        return self

    def is_loaded(self) -> 'LoginPage':
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_url(self.locators.url)
        self.page.wait_for_timeout(1000)
        return self

    def wait(self, timeout: float) -> 'LoginPage':
        self.page.wait_for_timeout(timeout)
        return self

    def open_login_form(self) -> 'LoginPage':
        self.locators.login_link.click()
        return self

    def fill_email(self, email: str, **kwargs) -> 'LoginPage':
        """Ввести email"""
        self.locators.email_field.fill(email)
        return self

    def click_continue(self) -> 'LoginPage':
        self.locators.continue_button.click()
        return self

    def fill_password(self, password: str, **kwargs) -> 'LoginPage':
        """Ввести пароль"""
        self.locators.password_field.fill(password)
        return self

    def submit(self) -> 'LoginPage':
        """Нажать кнопку submit"""
        self.locators.submit_button.click()
        return self

    def should_be_logged_in(self) -> 'LoginPage':
        """Проверить успешный логин"""
        expect(self.page).not_to_have_url(self.locators.url)
        return self
