# logger.py

import logging
from datetime import datetime
import os
from config import LOG_DIR

def setup_logger(name: str = "scraper") -> logging.Logger:
    """
    Configures and returns a logger instance with UTF-8 encoding for both file and console output.

    Args:
        name (str): Name of the logger.

    Returns:
        Logger: Configured logger instance.
    """
    os.makedirs(LOG_DIR, exist_ok=True)
    log_file = f"{LOG_DIR}/scraper_{datetime.now().strftime('%Y%m%d_%H%M')}.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.stream.reconfigure(encoding="utf-8")

    formatter = logging.Formatter('%(asctime)s — %(levelname)s — %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
