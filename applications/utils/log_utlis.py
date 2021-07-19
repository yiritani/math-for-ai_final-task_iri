import logging
import logging.config
import os

from applications.config import config_getter

config = config_getter.config_initialize()


def write_log(data):
    formatter = '%(asctime)s:%(message)s'
    logging.basicConfig(filename=config_getter.get_log_file_path(), encoding='utf-8', level=logging.INFO, format=formatter)
    logging.info(data)
