from dataclasses import dataclass
from typing import Optional

from models.login.user_credentials import UserCredentials


# Пример предустановленных данных (пресеты)
class Users:
    VALID_USER = UserCredentials(
        email="prod_user_01@rover.info",
        password="Oracle01",
        username="prod_user_01"
    )

    INVALID_PASSWORD = UserCredentials(
        email="prod_user_01@example.com",
        password="wrong_password"
    )
