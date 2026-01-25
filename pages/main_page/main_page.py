from dataclasses import dataclass

from playwright.sync_api import Page, expect
from locators.main_page_locators import MainPageLocators as Mpl


@dataclass
class MainPage:
    """Page Object для главной страницы"""
    page: Page
    url = "https://realt.by/"

    def is_loaded(self):
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_url(Mpl.URL.value)
        self.page.wait_for_timeout(1000)

    def click_add_adv(self):
        """Нажать кнопку 'Подать за 0 BYN'"""
        self.page.click(Mpl.ADD_ADV.value)
        # expect(self.page).to_have_url(url_or_reg_exp='https://realt.by/podat-obyavlenie/')
        self.page.wait_for_timeout(1000)

"""
Сравнение состояний загрузки (wait_for_load_state)

    Состояние, Что ждёт, Когда использовать, Скорость
    load, событие load (всё + картинки), Когда важны все ресурсы, Медленно
    domcontentloaded, "HTML распарсен, DOM готов", Когда достаточно структуры страницы, Быстро
    networkidle, нет сетевых запросов > 500 мс, Самый надёжный вариант для SPA и большинства сайтов, Средне
"""
