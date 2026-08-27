import os
import logging
from pathlib import Path
from loguru import logger

# Remove default handler
logger.remove()

# Log directory
log_dir = Path('logs')
log_dir.mkdir(exist_ok=True)

# Console handler
logger.add(
    lambda msg: print(msg, end=''),
    format="<level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level=os.getenv('LOG_LEVEL', 'INFO')
)

# File handler
logger.add(
    log_dir / 'video_processor.log',
    rotation="500 MB",
    retention="10 days",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG"
)

export { logger }
