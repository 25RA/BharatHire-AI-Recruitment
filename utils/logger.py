from pathlib import Path

from loguru import logger

LOG_DIR = Path("logs")

LOG_DIR.mkdir(exist_ok=True)

logger.add(
    LOG_DIR / "bharathire.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
    enqueue=True,
)

app_logger = logger