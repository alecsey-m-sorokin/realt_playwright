import pytest
from playwright.sync_api import sync_playwright


# @pytest.fixture(scope="session")
# def browser():
#     """Фикстура для запуска браузера (session scope)"""
#     playwright = sync_playwright().start()
#     browser = playwright.chromium.launch(headless=False)
#     yield browser
#     browser.close()
#     playwright.stop()
#
#
# @pytest.fixture(scope="function")
# def page(browser):
#     """Фикстура для новой страницы (function scope)"""
#     context = browser.new_context(
#         viewport={"width": 1280, "height": 800},
#         ignore_https_errors=True,
#     )
#     page = context.new_page()
#     yield page
#     page.close()
#     context.close()

# @pytest.fixture(scope="session", autouse=True)
# def browser_type_launch_args():
#     return {
#         "headless": False,
#         "args": [
#             "--start-maximized",
#             # "--window-size=`1920,1080",
#             # "--slow_mo=1000",
#             "--screenshot only - on - failure"
#         ]
#     }
#
# @pytest.fixture(scope="session", autouse=True)
# def browser_context_args():
#     return {
#         "no_viewport": False,
#         "viewport": {
#             "width": 1920,
#             "height": 1080,
#         },
#     }

@pytest.fixture(scope="session", autouse=True)
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "args": [
            "--start-maximized",
            # "--window-size=1920,1080",
            # "--window-size=3440,1440",
        ],
        # "slow_mo": 1000,
    }

@pytest.fixture(scope="session", autouse=True)
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 3440,
            "height": 1440,
            # "width": 1920,
            # "height": 1080,
        },
    }
