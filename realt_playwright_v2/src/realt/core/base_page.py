from __future__ import annotations

from dataclasses import dataclass, field

from playwright.sync_api import Locator, Page

from realt.config.settings import DEFAULT_TIMEOUT_MS
from realt.core.waits import Waits


@dataclass(frozen=True, slots=True)
class BasePage:
    page: Page
    timeout_ms: int = field(default=DEFAULT_TIMEOUT_MS, kw_only=True)

    @property
    def waits(self) -> Waits:
        return Waits(page=self.page, timeout_ms=self.timeout_ms)

    def open(self, url: str) -> "BasePage":
        self.page.goto(url)
        return self

    def click(self, locator: Locator) -> "BasePage":
        self.waits.visible(locator)
        locator.scroll_into_view_if_needed()
        locator.click()
        return self

    def fill(self, locator: Locator, value: str, *, clear: bool = True) -> "BasePage":
        self.waits.visible(locator)
        locator.scroll_into_view_if_needed()
        if clear:
            locator.clear()
        locator.fill(value)
        return self
