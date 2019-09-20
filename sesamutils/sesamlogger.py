import logging
import os
import paste.translogger


def sesam_logger(logger_name, app=None, timestamp=False):
    if logger_name is None or logger_name is '':
        raise ValueError('Please provide a valid logger name.')
    logger = logging.getLogger(logger_name)
    log_level = os.getenv('LOG_LEVEL')
    level = logging.getLevelName(log_level.upper()) if log_level is not None else None
    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                                                  if timestamp else '%(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(stdout_handler)
    # Comment these two lines if you don't want access request logging
    if app:
        app.wsgi_app = paste.translogger.TransLogger(app.wsgi_app, logger_name=logger.name, setup_console_handler=False)
        app.logger.addHandler(stdout_handler)
        logger.propagate = False
    if not isinstance(level, int):
        logger.warning("Unsupported value or no LOG_LEVEL provided. Hence, setting default log level to INFO.")
        level = logging.INFO
    logger.setLevel(level)
    return logger



