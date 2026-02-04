from dataclasses import dataclass

from pages.base_page.base_page import BasePage


@dataclass
class PropertyPage(BasePage):
    LOCATION_CONTAINER = "#location"
    OBJECT_CONTAINER = "#object"
    AREA_CONTAINER = "#area"
    HOUSE_CONTAINER = "#house"
    capacity_container = "#capacity"
    BATHROOM_CONTAINER = "#bathroom"
    RULES_CONTAINER = "#rules"
    MEDIA_CONTAINER = "#media"
    DESCRIPTION_CONTAINER = "#description"
    CONTACTS_CONTAINER = "#contacts"
