import logging
import sys
from logging.handlers import TimedRotatingFileHandler
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")


def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(FORMATTER)
   return console_handler


def get_file_handler(log_file):
   file_handler = TimedRotatingFileHandler(log_file, when='midnight')
   file_handler.setFormatter(FORMATTER)
   return file_handler


def get_logger(logger_name):
   loger = logging.getLogger(logger_name)
   loger.setLevel(logging.DEBUG) # better to have too much log than not enough
   loger.addHandler(get_console_handler())
   loger.addHandler(get_file_handler(logger_name))
   # with this pattern, it's rarely necessary to propagate the error up to parent
   loger.propagate = False
   return loger