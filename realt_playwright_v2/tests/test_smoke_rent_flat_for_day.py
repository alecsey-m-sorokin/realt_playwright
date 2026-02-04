from __future__ import annotations

import os

import pytest
from playwright.sync_api import Page

from realt.config.settings import Settings
from realt.models.credentials import Credentials
from realt.models.object_location import ObjectLocation
from realt.models.rent_flat_for_day import RentFlatForDayData
from realt.pages.login import LoginPage
from realt.pages.rent_flat_for_day import RentFlatForDayPage


@pytest.mark.ui
def test_smoke_login_and_open_form(page: Page, settings: Settings) -> None:
    email = os.getenv("REALT_EMAIL")
    password = os.getenv("REALT_PASSWORD")
    if not email or not password:
        pytest.skip("Set REALT_EMAIL and REALT_PASSWORD to run this smoke test")

    creds = Credentials(email=email, password=password)

    LoginPage(page=page, settings=settings).login(creds)

    data = RentFlatForDayData()
    location = ObjectLocation(
        settlement="минск",
        settlement_name="г. Минск Минский р-н, Минская область",
        street="берута",
        street_name="Берута ул",
        house_number="11",
        building_number="а",
    )

    RentFlatForDayPage(page=page, settings=settings).open_form().fill_location(
        location
    ).select_object_params(data).fill_area(data).fill_house(data).fill_capacity(data)
