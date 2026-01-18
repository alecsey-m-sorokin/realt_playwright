from enum import Enum


class User(Enum):
    """Тестовые пользователи для realt.by"""

    VALID = ("prod_user_01@rover.info", "Oracle01")
    WRONG_PASSWORD = ("prod_user_01@rover.info", "WrongPass123!")
    WRONG_EMAIL = ("nonexistent_999@rover.info", "Oracle01")
    EMPTY = ("", "")

    @property
    def email(self) -> str:
        """Email / логин пользователя"""
        return self.value[0]

    @property
    def password(self) -> str:
        """Пароль пользователя"""
        return self.value[1]

    @property
    def description(self) -> str:
        """Краткое описание сценария"""
        descriptions = {
            User.VALID: "Корректные учетные данные",
            User.WRONG_PASSWORD: "Существующий email + неверный пароль",
            User.WRONG_EMAIL: "Несуществующий email",
            User.EMPTY: "Пустые поля логина и пароля"
        }
        return descriptions.get(self, "Неизвестный сценарий")

    def __str__(self) -> str:
        return f"{self.name} ({self.description})"


if __name__ == "__main__":
    print(User.WRONG_PASSWORD)
