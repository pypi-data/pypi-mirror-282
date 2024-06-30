from datetime import datetime
import logging
import logging.handlers
import sys
import os

CURRENT_LEVEL = logging.INFO

def get_logger(log_path,
               filename: str = 'training',
               module_name: str = __file__,
               logger_level: int = CURRENT_LEVEL,
               stream_handler_level: int = CURRENT_LEVEL,
               file_handler_level: int = CURRENT_LEVEL):
    logger = logging.getLogger(module_name)
    logger.handlers.clear()
    logger.setLevel(logger_level)

    log_path = os.path.join(log_path, module_name, datetime.now().strftime('%Y%m%d'))
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "%Y/%m/%dT%H:%M:%S")

    fh = logging.FileHandler(os.path.join(log_path, filename + '.log'), 'a')
    fh.setLevel(file_handler_level)
    fh.setFormatter(format)
    logger.addHandler(fh)

    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(stream_handler_level)
    sh.setFormatter(format)
    logger.addHandler(sh)

    return logger