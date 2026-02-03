from dataclasses import dataclass

from pages.base_page.base_page import BasePage


@dataclass
class PropertyPage(BasePage):
    LOCATION_CONTAINER = "#location"
    OBJECT_CONTAINER = "#object"
