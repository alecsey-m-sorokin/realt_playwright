from pathlib import Path
from typing import Optional, Union
from screeninfo import get_monitors, ScreenInfoError

from loguru import logger

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
            ".gitignore",
            "pytest.ini",
            "conftest.py",
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


def get_monitor_resolution(monitor_index: int = None):
    """
    Получает разрешение монитора.
    Если monitor_index задан, берет монитор по индексу.
    Если не задан, ищет основной (is_primary).
    """
    # Стандартное разрешение для CI-сред или ошибок
    default_width, default_height = 1920, 1080
    selected_width, selected_height = None, None

    try:
        monitors = get_monitors()

        # Логируем все найденные мониторы для отладки
        for i, m in enumerate(monitors):
            logger.info(f"Доступен монитор [{i}]: {m.width}x{m.height}, Primary: {m.is_primary}")

        # 1. Если пользователь указал конкретный индекс
        if monitor_index is not None:
            if 0 <= monitor_index < len(monitors):
                target = monitors[monitor_index]
                selected_width, selected_height = target.width, target.height
                logger.info(f"Выбран монитор по индексу [{monitor_index}]")
            else:
                logger.warning(f"Индекс {monitor_index} не найден. Всего мониторов: {len(monitors)}")

        # 2. Если индекс не подошел или не был указан, ищем Primary
        if selected_width is None:
            for m in monitors:
                if m.is_primary:
                    selected_width, selected_height = m.width, m.height
                    logger.info(f"Выбран основной (Primary) монитор [{m}]")
                    break

        # 3. Если даже Primary не найден (бывает в некоторых ОС), берем первый из списка
        if selected_width is None and monitors:
            selected_width, selected_height = monitors[0].width, monitors[0].height
            logger.info("Primary не найден, выбран первый доступный монитор")

    except (ScreenInfoError, Exception) as e:
        logger.error(f"Ошибка при определении мониторов: {e}")

    # Финальная проверка: если ничего не нашлось, ставим дефолт
    final_w = selected_width or default_width
    final_h = selected_height or default_height

    logger.warning(f"ИТОГОВОЕ РАЗРЕШЕНИЕ: {final_w}x{final_h}")
    return final_w, final_h


if __name__ == "__main__":
    SCREEN_WIDTH, SCREEN_HEIGHT = get_monitor_resolution(monitor_index=None)
