import pathlib
from pathlib import Path
import os

from loguru import logger

if __name__ == "__main__":

    project_root = Path(__file__).resolve().parent.parent
    media_dir = project_root / "media_photos"
    base_dir = Path(__file__).resolve().parent
    photos = [
        (media_dir / "001.jpg"),
        (media_dir / "002.jpg"),
        (media_dir / "003.jpg"),
    ]


    logger.info(project_root)
    logger.info(media_dir)
    logger.info(base_dir)
    logger.info(photos)
    logger.info(Path(__file__).resolve().parent.parent)
    logger.info(Path(__file__).resolve().parent)
    logger.info(Path(__file__).resolve())
    logger.info(Path(__file__).resolve().parent.parent.parent)
    logger.info(Path(__file__).resolve().parents[1])

    def get_project_root():
        current = Path(__file__).resolve()
        while current != current.parent:
            if (current / "pyproject.toml").exists() or \
               (current / ".git").exists() or \
               (current / "poetry.lock").exists():
                return current
            current = current.parent
        raise RuntimeError("Не удалось найти корень проекта")
    root_dir = get_project_root()
    logger.info(root_dir)
    logger.warning(Path.cwd())


    def get_project_root_v2() -> Path:
        """
        Предполагаем, что файл находится где-то внутри папки tests/
        """
        current = Path(__file__).resolve()

        # Поднимаемся вверх, пока не найдём папку tests
        while current.name != "tests" and current != current.parent:
            current = current.parent

        # Теперь поднимаемся ещё на один уровень — это и есть корень
        root = current.parent

        # Проверяем, что мы действительно нашли tests
        if (root / "tests").exists():
            return root

        raise RuntimeError("Не удалось определить корень проекта. Убедитесь, что файл внутри папки tests")

    root_dir = get_project_root_v2()
    logger.debug(root_dir)
