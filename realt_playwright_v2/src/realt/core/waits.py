from __future__ import annotations

from dataclasses import dataclass

from playwright.sync_api import Locator, Page, expect


@dataclass(frozen=True, slots=True)
class Waits:
    page: Page
    timeout_ms: int

    def visible(self, locator: Locator) -> Locator:
        expect(locator).to_be_visible(timeout=self.timeout_ms)
        return locator

    def hidden(self, locator: Locator) -> Locator:
        expect(locator).to_be_hidden(timeout=self.timeout_ms)
        return locator

    def url_is(self, url: str) -> None:
        expect(self.page).to_have_url(url, timeout=self.timeout_ms)

    def url_contains(self, fragment: str) -> None:
        expect(self.page).to_have_url(f"*{fragment}*", timeout=self.timeout_ms)
