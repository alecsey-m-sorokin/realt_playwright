from dataclasses import dataclass
from typing import Optional

from models.object_location_model import ObjectLocationModel


# Пример предустановленных данных (пресеты)
class ObjectLocationsTestData:
    MINSK_BERUTA_11_A = ObjectLocationModel(
        settlement="Минск",
        settlement_name="г. Минск Минский р-н, Минская область",
        street="Берута",
        street_name='Берута ул',
        house_number="11",
        building_number="A"
    )
