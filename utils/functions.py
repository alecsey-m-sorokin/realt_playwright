from pathlib import Path
from typing import Optional, Union

from loguru import logger


# def get_project_root() -> Path:
#     """ Предполагаем, что файл находится где-то внутри папки tests/ """
#     current = Path(__file__).resolve()
#     logger.info(current)
#
#     # Поднимаемся вверх, пока не найдём папку tests
#     while current.name != "tests" and current != current.parent:
#         current = current.parent
#
#     # Теперь поднимаемся ещё на один уровень — это и есть корень
#     root = current.parent
#
#     # Проверяем, что мы действительно нашли tests
#     if (root / "tests").exists():
#         return root
#
#     raise RuntimeError("Не удалось определить корень проекта. Убедитесь, что файл внутри папки tests")


# def get_project_root() -> Path:
#     current = Path(__file__).resolve()
#
#     # Ищем папку tests, поднимаясь вверх
#     while current.name != "tests" and current != current.parent:
#         print(current.name)
#         current = current.parent
#
#     if current.name == "tests":
#         return current.parent  # возвращаем корень проекта (родитель папки tests)
#
#     # Если tests не нашли — fallback на корень по количеству родителей
#     return Path(__file__).resolve().parents[3]

# def get_project_root() -> Path | None:
#     current = Path(__file__).resolve()
#
#     markers = {
#         "pyproject.toml",
#         "poetry.lock",  # у тебя есть этот файл в корне
#         ".git",
#         "pytest.ini",
#         "requirements.txt",
#     }
#
#     while current != current.parent:
#         if any((current / marker).exists() for marker in markers):
#             return current
#         current = current.parent

def get_project_root(custom_marker: Optional[Union[str, Path]] = None) -> Path:
    """
    Находит корень проекта, поднимаясь вверх по директориям до первого найденного маркера.

    Args:
        custom_marker: Если указан — ищет только этот файл/папку.
                       Может быть строкой (имя файла) или Path.
                       Если None — используются маркеры по умолчанию.

    Returns:
        Path: Абсолютный путь к корню проекта

    Raises:
        RuntimeError: Если корень проекта не удалось определить
    """
    current = Path(__file__).resolve()

    # Определяем, что будем искать
    if custom_marker is not None:
        markers = {Path(custom_marker).name}  # берём только имя
    else:
        markers = {
            "pyproject.toml",
            "poetry.lock",
            "setup.py",
            "setup.cfg",
            ".git",
            "pytest.ini",
            "requirements.txt",
        }

    while current != current.parent:
        if any((current / marker).exists() for marker in markers):
            return current
        current = current.parent

    raise RuntimeError(
        "Не удалось определить корень проекта.\n"
        f"Не найден ни один из маркеров: {', '.join(markers)}\n"
        "Убедитесь, что запускаемый файл находится внутри структуры проекта "
        "и хотя бы один из ожидаемых маркеров присутствует в корне."
    )