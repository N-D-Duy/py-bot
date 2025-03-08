import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Create logs directory if it doesn't exist
logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)

# Configure logger
def setup_logger(name="bot_logger", level=logging.INFO):
    """
    Set up a logger that writes error logs to logs/bot.txt

    Args:
        name (str): Name of the logger
        level (int): Logging level

    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Clear any existing handlers to prevent duplicate logs
    if logger.handlers:
        logger.handlers.clear()

    # Create file handler for error logs
    error_handler = RotatingFileHandler(
        "logs/bot.txt",
        maxBytes=10_485_760,  # 10MB
        backupCount=5,
        encoding="utf-8"
    )
    error_handler.setLevel(logging.ERROR)

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Add formatter to handler
    error_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(error_handler)

    # Optional console handler for non-error logs during development
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

# Default logger instance
logger = setup_logger()