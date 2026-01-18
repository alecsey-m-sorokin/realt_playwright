from enum import Enum


class UploadPhotosPageLocators(Enum):
    """Локаторы для страницы загрузки фото
    """

    URL = "https://realt.by/"
    ADD_ADV = 'button:has-text("Подать за 0 BYN"):not(.lg\\:hidden)'

    SELECT_PHOTOS_BUTTON = 'button:has-text("Выберите фотографии")'
    UUID_INPUTS = 'input[name^="media.photos."][name$=".uuid"]'

    PHOTOS = [
        r"media_photos/001.jpg",
        r"media_photos/002.jpg",
        r"media_photos/003.jpg",
    ]
