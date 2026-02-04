from __future__ import annotations

from loguru import logger
from screeninfo import ScreenInfoError, get_monitors


def get_monitor_resolution() -> tuple[int, int]:
    default_width, default_height = 1920, 1080

    try:
        monitors = get_monitors()
        for i, monitor in enumerate(monitors):
            logger.debug(
                "Monitor[{}]: {}x{}, primary={}",
                i,
                monitor.width,
                monitor.height,
                getattr(monitor, "is_primary", False),
            )

        primary = next(
            (
                m
                for m in monitors
                if getattr(m, "is_primary", False)
            ),
            None,
        )
        target = primary or (monitors[0] if monitors else None)
        if target is None:
            return default_width, default_height

        return int(target.width), int(target.height)
    except (ScreenInfoError, Exception) as exc:
        logger.warning("Failed to detect monitor resolution: {}", exc)
        return default_width, default_height
