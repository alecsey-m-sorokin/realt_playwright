from __future__ import annotations

import os

import pytest
from loguru import logger

from realt.config.settings import Settings


@pytest.fixture(scope="session")
def settings() -> Settings:
    return Settings.from_env()


@pytest.fixture(scope="session", autouse=True)
def browser_type_launch_args(browser_type_launch_args: dict, settings: Settings) -> dict:
    return {
        **browser_type_launch_args,
        "headless": settings.headless,
        "slow_mo": settings.slow_mo_ms or None,
        "args": [
            f"--window-size={settings.viewport_width},{settings.viewport_height}",
            "--start-maximized",
        ],
    }


@pytest.fixture(scope="session", autouse=True)
def browser_context_args(browser_context_args: dict, settings: Settings) -> dict:
    return {
        **browser_context_args,
        "viewport": {"width": settings.viewport_width, "height": settings.viewport_height},
        "ignore_https_errors": True,
    }


def pytest_configure() -> None:
    logger.info("REALT_BASE_URL={}", os.getenv("REALT_BASE_URL", "https://realt.by"))
