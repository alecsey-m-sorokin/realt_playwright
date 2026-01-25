from dataclasses import dataclass
from typing import List, Any

from loguru import logger
from playwright.sync_api import Page, expect

from locators.media_page.upload_photos_page_locators import UploadPhotosPageLocators


@dataclass
class UploadMediaPage:
    """Page Object для страницы 'Подать объявление - продажа квартира - загрузка фото'"""

    page: Page
    file_chooser_timeout = 15000
    upload_verification_timeout = 30000
    post_upload_delay = 3000
    locators: UploadPhotosPageLocators

    def upload_photos(self, photos: List[str]):
        """Загружает фотографии и проверяет их отображение на странице"""

        # Ожидаем вызов системного диалога выбора файлов
        with self.page.expect_file_chooser(timeout=self.file_chooser_timeout) as fc_info:
            self.locators.select_photos_button.click()

        # Загружаем файлы
        file_chooser = fc_info.value
        file_chooser.set_files(files=photos, timeout=self.file_chooser_timeout)

        # Проверяем успешность загрузки
        self._verify_upload_completion(files=photos)

    def _verify_upload_completion(self, files: Any) -> None:
        expected_count = len(files)
        uuid_inputs = self.page.locator(selector=self.locators.uuid_inputs)
        expect(uuid_inputs).to_have_count(count=expected_count, timeout=self.upload_verification_timeout)
        self.page.wait_for_timeout(self.post_upload_delay)
        logger.info(f"Загружено фотографий : {uuid_inputs.count()}")
