import logging
import logging.config

from otameshi.config import config_getter

config = config_getter.config_initialize()


def write_log(file, data=None):
    formatter = '%(asctime)s:%(message)s'
    logging.basicConfig(filename=config_getter.get_log_file_path(), encoding='utf-8', level=logging.INFO, format=formatter)
    logging.info(file + ' ' + data)
