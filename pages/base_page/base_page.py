from dataclasses import dataclass
from typing import Union, Callable, Literal, Optional

from loguru import logger
from playwright.sync_api import Page, expect, Locator

from locators.base_page.base_page_locators import BasePageLocators
from locators.sell.residential.sell_residential_flat_locators import SellResidentialFlatLocators
from models.object_location_model import ObjectLocationModel

# Типизация ролей для подсказок в IDE
RoleType = Literal["button", "link", "menuitem", "tab", "checkbox", "radio"]


@dataclass
class BasePage:
    """Page Object для страницы 'base_page'"""

    page: Page
    wait_timeout = 1000
    common_delay = 500
    locators: BasePageLocators

    def __getattr__(self, name):
        # Проверяем, есть ли такой метод у объекта page
        attr = getattr(self.page, name)
        if callable(attr):
            def wrapper(*args, **kwargs):
                attr(*args, **kwargs)
                return self
            return wrapper
        return attr

    def execute(self, action: Callable[[Page], None]) -> 'BasePage':
        """Выполняет любое действие с page и возвращает self
        :param action: Действие, которое нужно выполнить
        :return: self
        :example: execute(lambda p: p.wait_for_timeout(timeout=500))
        :example: self.execute(lambda p: p.locator("#object").get_by_text(text=object_rooms, exact=True).click())
        """
        action(self.page)
        return self

    def locate_element(self, name: str, by_role: bool = True) -> Locator:
        if by_role:
            return self.page.get_by_role(role="button", name=name)
        return self.page.get_by_text(name, exact=True)

    def get_named_element(self, name: str, role: Optional[RoleType] = "button", root: Optional[Union[Locator, str]] = None, exact: bool = True) -> Locator:
        """
        Универсальный поиск элемента по имени (label) с поддержкой ролей и контейнеров с автоматическим фоллбеком.
        Если указана роль, но такой элемент не найден за короткое время,
        метод переключится на поиск по тексту.

        :param name: Текст, который отображается на элементе или связан с ним.
        :param role: ARIA-роль элемента (button, link и т.д.).
                     Если передать None, поиск пойдет только по тексту (get_by_text).
        :param root: Родительский контейнер. Может быть строкой-селектором (например, "#id")
                     или уже созданным локатором. Если не указан, поиск идет по всей странице.
        :param exact: Флаг строгого соответствия текста (по умолчанию True).
        :return: Объект Locator для дальнейшего взаимодействия.
        """
        if isinstance(root, str):
            base = self.page.locator(root)
        elif isinstance(root, Locator):
            base = root
        else:
            base = self.page

        # Если роль не указана изначально — ищем просто по тексту
        if not role:
            logger.info(f"Finding element '{name}' by text-only (no role)")
            return base.get_by_text(name, exact=exact)

        # Пытаемся найти по роли
        role_locator = base.get_by_role(role=role, name=name, exact=exact)

        try:
            # Короткая проверка: есть ли такой элемент с ролью в DOM?
            # Используем count(), так как он не ждет 30 секунд, в отличие от is_visible()
            if role_locator.count() > 0:
                logger.info(f"Found element '{name}' as ROLE '{role}'")
                return role_locator
        except Exception:
            pass

        # Если по роли не нашли — откатываемся к тексту
        logger.info(f"Role '{role}' not found for '{name}'. Falling back to text-only search.")
        return base.get_by_text(name, exact=exact)

    def _wait_and_fill(
            self,
            locator: Union[Locator, str],
            value: str,
            timeout: int = wait_timeout,
            clear: bool = True
    ) -> None:
        """Метод с проверкой редактируемости и центрированием элемента"""
        element = self.page.locator(locator) if isinstance(locator, str) else locator

        # 1. Ждем появления в DOM
        element.wait_for(state="attached", timeout=timeout)

        # 2. Скроллим так, чтобы элемент оказался в центре (помогает избежать перекрытия хедером)
        element.evaluate("el => el.scrollIntoView({ block: 'center', inline: 'nearest' })")

        # 3. Проверяем, можно ли в поле вводить текст
        # fill() сам делает проверку, но явное ожидание дает более понятную ошибку при падении
        if not element.is_editable(timeout=timeout):
            raise Exception(f"Элемент {locator} не доступен для редактирования")

        if clear:
            element.clear()

        element.fill(str(value))

        if self.common_delay:
            self.page.wait_for_timeout(self.common_delay)

    def _wait_and_click(
            self,
            locator: Union[Locator, str],
            timeout: int = wait_timeout
    ) -> None:
        """
        Общий метод для клика по элементу с центрированием
        и проверкой доступности для нажатия.
        """
        # 1. Подготовка локатора
        element = self.page.locator(locator) if isinstance(locator, str) else locator

        # 2. Ждем появления в DOM
        element.wait_for(state="attached", timeout=timeout)

        # 3. Скроллим элемент в центр экрана
        # Это минимизирует риск того, что элемент перекроет фиксированный хедер или футер
        element.evaluate("el => el.scrollIntoView({ block: 'center', inline: 'nearest' })")

        # 4. Проверка на видимость и стабильность (actionability)
        # click() в Playwright автоматически ждет, пока элемент станет кликабельным,
        # но явный вызов scroll + wait_for(visible) делает процесс более предсказуемым.
        element.wait_for(state="visible", timeout=timeout)

        # 5. Клик
        # Мы используем встроенные проверки Playwright (visible, enabled, stable, receive events)
        element.click(timeout=timeout)

        # 6. Задержка, если она задана
        if self.common_delay:
            self.page.wait_for_timeout(self.common_delay)

    # def _wait_and_fill(self, locator: Union[Locator, str], value: str, timeout: int = wait_timeout, clear: bool = True) -> None:
    #     """Общий метод для заполнения полей ввода"""
    #     element = self.page.locator(locator) if isinstance(locator, str) else locator
    #     element.wait_for(state="visible", timeout=timeout)
    #
    #     element.scroll_into_view_if_needed()
    #     element.clear() if clear else None
    #     element.fill(str(value))
    #     self.page.wait_for_timeout(self.common_delay)

    # def _wait_and_click(self, locator: Union[Locator, str], timeout: int = wait_timeout) -> None:
    #     """Общий метод для клика по элементу"""
    #     element = self.page.locator(locator) if isinstance(locator, str) else locator
    #     element.wait_for(state="visible", timeout=timeout)
    #     element.scroll_into_view_if_needed()
    #     element.click()
    #     self.page.wait_for_timeout(self.common_delay)

    def is_loaded(self, url: str):
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_url(url)
        self.page.wait_for_timeout(1000)
        return self

    def wait(self, timeout: float):
        self.page.wait_for_timeout(timeout)
        return self

    def open(self, url: str):
        """Открыть страницу"""
        self.page.goto(url)
        return self

    def click_add_adv(self):
        """Нажать кнопку 'Подать за 0 BYN'"""
        self.page.get_by_role(role="button", name="Добавить объявление").click()
        self.page.wait_for_timeout(1000)
        return self

    def fill_location(self):

        return self

    @property
    def location(self):
        """Позволяет обращаться к методам как page.location.fill_settlement(...)"""
        return self.Location(self)


    @dataclass
    class Location:

        base: BasePage

        def fill_location_settlement(self, settlement: str, settlement_name) -> 'BasePage.Location':
            """Заполнить поле 'Населенный пункт, район, область'"""
            self.base._wait_and_fill(locator=self.base.locators.location_settlement, value=settlement)
            self.base._wait_and_click(locator=self.base.locate_element(settlement_name))
            return self

        def fill_location_street(self, street: str, street_name) -> 'BasePage.Location':
            """Заполнить поле 'Улица'"""
            self.base._wait_and_fill(locator=self.base.locators.location_street, value=street)
            self.base._wait_and_click(locator=self.base.locate_element(street_name))
            return self

        def fill_location_house_number(self, house_number: str) -> 'BasePage.Location':
            """Заполнить поле 'Дом'"""
            self.base._wait_and_fill(locator=self.base.locators.location_house_number, value=house_number)
            return self

        def fill_location_building_number(self, building_number: str) -> 'BasePage.Location':
            """Заполнить поле 'Корпус'"""
            self.base._wait_and_fill(locator=self.base.locators.location_building_number, value=building_number)
            return self

        def parent(self):
            """Метод для выхода из Location обратно в BasePage"""
            return self.base

        def fill_location(self, object_location: ObjectLocationModel):
            self.fill_location_settlement(settlement=object_location.settlement, settlement_name=object_location.settlement_name) \
                .fill_location_street(street=object_location.street, street_name=object_location.street_name) \
                .fill_location_house_number(house_number=object_location.house_number) \
                .fill_location_building_number(building_number=object_location.building_number)
            return self
