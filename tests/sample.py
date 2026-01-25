from playwright.sync_api import Playwright, sync_playwright, ViewportSize

from locators.media_page.upload_photos_page_locators import UploadPhotosPageLocators
from pages.media_page.upload_photos_page import UploadMediaPage
from utils.functions import get_project_root, get_monitor_resolution

SCREEN_WIDTH, SCREEN_HEIGHT = get_monitor_resolution()


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(
        headless=False,
        args=[f"--window-size={SCREEN_WIDTH},{SCREEN_HEIGHT}, --start-maximized"]
    )
    context = browser.new_context(
        viewport=ViewportSize(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    )
    page = context.new_page()
    page.goto("https://realt.by/")
    page.get_by_role("link", name="Войти").click()
    page.get_by_role("textbox", name="Email / логин / +").click()
    page.get_by_role("textbox", name="Email / логин / +").fill("prod_user_01@rover.info")
    page.get_by_role("button", name="Продолжить").click()
    page.get_by_role("textbox", name="Введите пароль").click()
    page.get_by_role("textbox", name="Введите пароль").fill("Oracle01")
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("button", name="Добавить объявление").click()
    page.get_by_role("button", name="Сдать длительно").click()
    page.get_by_role("button", name="Жилая").click()
    page.get_by_role("button", name="Квартира").click()
    page.get_by_role("textbox", name="Адрес").click()
    page.get_by_role("textbox", name="Адрес").fill("Минск")
    page.get_by_role("button", name="г. Минск Минский р-н, Минская область").click()
    page.get_by_role("textbox", name="Улица").click()
    page.get_by_role("textbox", name="Улица").fill("Берута")
    page.get_by_role("button", name="Берута ул").click()
    page.get_by_role("textbox", name="Дом", exact=True).click()
    page.get_by_role("textbox", name="Дом", exact=True).fill("11")
    page.get_by_role("textbox", name="Корпус").click()
    page.get_by_role("textbox", name="Корпус").fill("а")
    page.get_by_role("button", name="4").click()
    page.get_by_role("textbox", name="Раздельных комнат").click()
    page.get_by_role("textbox", name="Раздельных комнат").fill("4")
    page.get_by_role("textbox", name="Этаж", exact=True).click()
    page.get_by_role("textbox", name="Этаж", exact=True).fill("9")
    page.get_by_role("button", name="Евроремонт").click()
    page.get_by_role("button", name="Балкон и лоджия").click()
    page.get_by_role("textbox", name="Площадь общая, м²").click()
    page.get_by_role("textbox", name="Площадь общая, м²").fill("138")
    page.get_by_role("textbox", name="Площадь жилая, м²").click()
    page.get_by_role("textbox", name="Площадь жилая, м²").fill("88")
    page.get_by_role("textbox", name="Этажей в доме").click()
    page.get_by_role("textbox", name="Этажей в доме").fill("16")
    page.get_by_role("textbox", name="Год постройки").click()
    page.get_by_role("textbox", name="Год постройки").fill("2010")
    page.get_by_role("button", name="Парковка").click()
    page.get_by_role("button", name="Есть").first.click()
    page.get_by_role("button", name="1 телефон").click()
    page.get_by_role("button", name="Плита электрическая").click()
    page.get_by_role("button", name="USD").click()
    page.get_by_role("textbox", name="За месяц").click()
    page.get_by_role("textbox", name="За месяц").fill("800")
    page.get_by_role("button", name="100%").click()
    page.get_by_role("button", name="Длительный").click()
    page.get_by_role("button", name="2 месяца", exact=True).click()
    page.get_by_role("button", name="Семье").click()
    # page.get_by_role("button", name="Выберите фотографии").click()


    file_chooser_timeout = 15000
    project_root = get_project_root()
    photos = [(project_root / item).as_posix() for item in UploadPhotosPageLocators.PHOTOS.value]

    # with page.expect_file_chooser(timeout=file_chooser_timeout) as fc_info:
    #     page.locator(selector=UploadPhotosPageLocators.SELECT_PHOTOS_BUTTON.value).click()
    # file_chooser = fc_info.value
    # file_chooser.set_files(files=photos, timeout=file_chooser_timeout)

    UploadMediaPage(page).upload_photos(photos)

    # page.get_by_role("button", name="Выберите фотографии").set_input_files(files=photos, timeout=15000)
    page.get_by_role("textbox", name="Краткое описание").click()
    page.get_by_role("textbox", name="Краткое описание").fill("это краткое описание для тестового объекта при подаче в длительной аренде !")
    page.get_by_role("textbox", name="Телефон").click()
    page.get_by_role("textbox", name="Телефон").press("ArrowRight")
    page.get_by_role("textbox", name="Телефон").press("ArrowRight")
    page.get_by_role("textbox", name="Телефон").press("ArrowRight")
    page.get_by_role("textbox", name="Телефон").press("ArrowRight")
    page.get_by_role("textbox", name="Телефон").press("ArrowRight")
    page.get_by_role("textbox", name="Телефон").press("ArrowRight")
    page.get_by_role("textbox", name="Телефон").fill("+375(29)664-53-11_")
    page.get_by_role("textbox", name="Имя (контактное)").click()
    page.get_by_role("button", name="Сохранить и продолжить").click()
    page.wait_for_timeout(10000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

if __name__ == "__main__":

    pass
