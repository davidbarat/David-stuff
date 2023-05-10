import logging
from logging.handlers import RotatingFileHandler
from logging import handlers

logger = logging.getLogger('portail')
logger.setLevel(logging.DEBUG)


fh = handlers.RotatingFileHandler(
    'C:\\',
    maxBytes=20000,
    backupCount = 5
)


formatter = logging.Formatter(
    '%(ascitime)s | %(levelname)s | %(name)s | %(message)s')

fh.setFormatter(formatter)

logger.addHandler(fh)
