from __future__ import annotations

from dataclasses import dataclass

from playwright.sync_api import Locator, Page


@dataclass(frozen=True, slots=True)
class LoginLocators:
    page: Page

    @property
    def login_link(self) -> Locator:
        return self.page.get_by_role("link", name="Войти")

    @property
    def email_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Email / логин / +")

    @property
    def continue_button(self) -> Locator:
        return self.page.get_by_role("button", name="Продолжить")

    @property
    def password_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Введите пароль")

    @property
    def submit_button(self) -> Locator:
        return self.page.get_by_role("button", name="Войти")
