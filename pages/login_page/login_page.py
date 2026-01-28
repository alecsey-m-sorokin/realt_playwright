from dataclasses import dataclass

from loguru import logger
from playwright.sync_api import Page, expect

from locators.login_page.login_page_locators import LoginPageLocators
from models.login.user_credentials import UserCredentials
from pages.base_page.base_page import BasePage


@dataclass
class LoginPage(BasePage):

    page: Page
    locators: LoginPageLocators

    @property
    def and_(self) -> 'LoginPage':
        return self

    def open_login_form(self) -> 'LoginPage':
        self.locators.login_link.click()
        return self

    def fill_email(self, email: str) -> 'LoginPage':
        """Ввести email"""
        self.locators.email_field.fill(email)
        return self

    def click_continue(self) -> 'LoginPage':
        self.locators.continue_button.click()
        return self

    def fill_password(self, password: str) -> 'LoginPage':
        """Ввести пароль"""
        self.locators.password_field.fill(password)
        return self

    def submit(self) -> 'LoginPage':
        """Нажать кнопку submit"""
        self.locators.submit_button.click()
        return self

    def should_be_logged_in(self, url) -> 'LoginPage':
        """Проверить успешный логин"""
        expect(self.page).not_to_have_url(url)
        return self

    def login(self, user: UserCredentials):
        self.open(url=self.locators.url) \
            .is_loaded(url=self.locators.url) \
            .fill_email(email=user.email) \
            .click_continue() \
            .wait(100) \
            .fill_password(password=user.password) \
            .submit() \
            .wait(100) \
            .should_be_logged_in(url=self.locators.url)
        return self
