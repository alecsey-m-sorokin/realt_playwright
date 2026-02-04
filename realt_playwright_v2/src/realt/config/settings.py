from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Final

from loguru import logger

from realt.core.viewport import get_monitor_resolution


@dataclass(frozen=True, slots=True)
class Settings:
    """Runtime settings for UI tests.

    Environment variables:
        REALT_BASE_URL: Base URL.
        REALT_HEADLESS: 1/0.
        REALT_SLOW_MO_MS: int.
        REALT_VIEWPORT: "WIDTHxHEIGHT". If not set, uses primary monitor.

    """

    base_url: str
    headless: bool
    slow_mo_ms: int
    viewport_width: int
    viewport_height: int

    @staticmethod
    def from_env() -> "Settings":
        base_url = os.getenv("REALT_BASE_URL", "https://realt.by")

        headless_raw = os.getenv("REALT_HEADLESS", "0").strip().lower()
        headless = headless_raw in {"1", "true", "yes", "y"}

        slow_mo_ms = int(os.getenv("REALT_SLOW_MO_MS", "0"))

        viewport_raw = os.getenv("REALT_VIEWPORT", "").strip().lower()
        if viewport_raw:
            try:
                w_str, h_str = viewport_raw.split("x", maxsplit=1)
                viewport_width = int(w_str)
                viewport_height = int(h_str)
            except ValueError as exc:
                raise ValueError(
                    "Invalid REALT_VIEWPORT, expected format 'WIDTHxHEIGHT'"
                ) from exc
        else:
            viewport_width, viewport_height = get_monitor_resolution()

        logger.debug(
            "Settings: base_url={}, headless={}, slow_mo_ms={}, viewport={}x{}",
            base_url,
            headless,
            slow_mo_ms,
            viewport_width,
            viewport_height,
        )

        return Settings(
            base_url=base_url,
            headless=headless,
            slow_mo_ms=slow_mo_ms,
            viewport_width=viewport_width,
            viewport_height=viewport_height,
        )


DEFAULT_TIMEOUT_MS: Final[int] = 10_000
