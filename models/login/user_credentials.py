from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class UserCredentials:
    """DTO для хранения данных пользователя."""
    email: str
    password: str
    username: Optional[str] = None  # Необязательное поле, если нужно для проверок
