import logging
from logging.handlers import RotatingFileHandler
from logging import handlers

# create logger
logger = logging.getLogger('selenium log')
logger.setLevel(logging.DEBUG)

# create filehandler
fh = handlers.RotatingFileHander(
    'C:\David\Selenium\log\selenium.log',
    maxBytes=20000,
    backupCount=5)

# create formatter
formatter = logging.Formatter(
    '%(asctime)s | %(levelname)s | %(name)s | %(message)s')

fh.setFormatter(formatter)

# add fh to logger
logger.addHandler(fh)
