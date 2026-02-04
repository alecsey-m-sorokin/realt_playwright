from __future__ import annotations

from dataclasses import dataclass

from playwright.sync_api import Page
from playwright.sync_api import expect

from realt.config.settings import Settings
from realt.core.base_page import BasePage
from realt.locators.login import LoginLocators
from realt.models.credentials import Credentials


@dataclass(frozen=True, slots=True)
class LoginPage(BasePage):
    page: Page
    settings: Settings

    @property
    def locators(self) -> LoginLocators:
        return LoginLocators(page=self.page)

    def open(self) -> "LoginPage":
        self.page.goto(f"{self.settings.base_url}/login/?nextPage=/")
        return self

    def login(self, credentials: Credentials) -> "LoginPage":
        self.open()

        login_url = self.page.url

        self.click(self.locators.login_link)
        self.fill(self.locators.email_field, credentials.email)
        self.click(self.locators.continue_button)

        self.fill(self.locators.password_field, credentials.password)
        self.click(self.locators.submit_button)

        expect(self.page).not_to_have_url(login_url, timeout=self.timeout_ms)
        return self
