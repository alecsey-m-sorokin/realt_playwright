from enum import Enum


class   SellFlatAddAdvLocators(Enum):
    """Локаторы для страницы - 'Подать объявление продажа квартиры' """

    URL = "https://realt.by/podat-obyavlenie/"

    CONTAINER = 'h1, h2, .text-h1, .text-h2:text("Тип объявления")'
    # expect(self.page.get_by_text("Подать объявление", exact=True)).to_be_visible(timeout=15000)  # ok
    # expect(self.page.get_by_label("Адрес")).to_be_visible(timeout=15000)  # ok
    # expect(self.page.get_by_text("Тип объявления", exact=True).first).to_be_visible(timeout=15000)  # ok (быстрый костыль, но рабочий)
    # expect(self.page.locator('span:not(.underline):text("Тип объявления")')).to_be_visible(timeout=15000)  # ok

    LOCATION_SETTLEMENT = '//*[@id="location.settlement"]'
    LOCATION_STREET = '//*[@id="location.street"]'
    LOCATION_DROPDOWN = 'li, div[role="option"], div, span'
    HOUSE_NUMBER = '//*[@id="location.houseNumber"]'
    BUILDING_NUMBER = '//*[@id="location.buildingNumber"]'
    APARTMENT_ROOMS = '//*[@id="apartment"]//*[text()="{rooms}"]'
    # self.page.get_by_role("button").filter(has_text="3").click()  # ok
    # self.page.locator('//div[contains(@class, "rooms") or contains(@class, "komnat")] //button | //div[@role="button"]' '[normalize-space(.)="3"]').click()  # ok
    # self.page.locator('div.flex > button:text("3"), div.flex > div[role="button"]:text("3")').first.click()  # ok
    # self.page.locator(f'//*[@id="apartment"]//*[text()="{rooms}"]').click()  # ok
    SEPARATE_ROOMS = '//*[@id="apartment.separateRooms"]'
    APARTMENT_STOREY = '//*[@id="apartment.storey"]'
    APARTMENT_BALCONY = '//*[@id="apartment"]//*[text()="{balcony}"]'
    AREA_TOTAL = '//*[@id="area.total"]'
    AREA_LIVING = '//*[@id="area.living"]'
    HOUSE_STOREYS = '//*[@id="house.storeys"]'
    HOUSE_BUILDING_YEAR = '//*[@id="house.buildingYear"]'
    CURRENCY = '//*[@id="termsOfDeal"]//*[text()="{currency}"]'
    PRICE = '//*[@id="termsOfDeal.price"]'
    OWNERSHIP = '//*[@id="termsOfDeal"]//*[text()="{ownership}"]'
    TERMS_OF_DEAL = '//*[@id="termsOfDeal"]//*[text()="{terms_of_deal}"]'
    SHORT_DESCRIPTION = 'textarea#description\\.shortDescription'
    # self._wait_and_fill(locator='textarea[placeholder*="грамотно описывает ваш объект"]', value=short_description)  # ok
    PHONES = 'input[name^="contacts.phones"], input[name^="phones"]'
    CONTACTS_NAME = 'input[name^="contacts.name"]'
    SAVE_AND_CONTINUE = 'button:has-text("Сохранить и продолжить")'
