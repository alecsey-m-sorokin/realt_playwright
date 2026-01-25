from dataclasses import dataclass

from playwright.sync_api import Page, Locator

@dataclass
class UploadPhotosPageLocators:
    """Локаторы для страницы - 'Подать объявление продажа квартиры'"""

    page: Page
    wait_timeout = 5000
    common_delay = 1000

    photos = [
        r"media_photos/001.jpg",
        r"media_photos/002.jpg",
        r"media_photos/003.jpg",
    ]

    def __init__(self, page: Page):
        self.page = page
        self.select_photos_button = page.get_by_role("button", name="Выберите фотографии")
        self.uuid_inputs = 'input[name^="media.photos."][name$=".uuid"]'
