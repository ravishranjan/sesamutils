import logging
import os


def sesam_logger(logger_name, timestamp=False):
    logger = logging.getLogger(logger_name)
    level = None
    if os.getenv('LOG_LEVEL') is not None:
        level = logging.getLevelName(os.getenv('LOG_LEVEL').upper())
    stdout_handler = logging.StreamHandler()
    if timestamp:
        stdout_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    else:
        stdout_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))

    logger.addHandler(stdout_handler)
    if not isinstance(level, int):
        logger.warning("Unsupported value or no LOG_LEVEL provided.Hence, setting default log level to 'INFO'")
        level = logging.INFO
    logger.setLevel(level)
    return logger

