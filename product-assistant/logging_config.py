import logging
from pathlib import Path
 
LOG_DIR = Path(__file__).parent / "logs"
LOG_FILE = LOG_DIR / "app.log"
 
 
def get_logger() -> logging.Logger:
    """Return the app logger. Writes to logs/app.log (set up once)."""
    logger = logging.getLogger("product_assistant")
 
    if logger.handlers:
        return logger
 
    LOG_DIR.mkdir(exist_ok=True)
 
    handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    handler.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    )
 
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.propagate = False 
    return logger
 