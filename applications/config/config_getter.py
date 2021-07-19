import os.path
from pathlib import Path
import yaml


def config_initialize():
    path = Path(__file__).parent
    with open(str(path) + '/config.yml') as yml:
        config = yaml.load(yml)

    return config


def get_backup_directory() -> str:
    return os.path.abspath('../ML_learning/templates/backup') + '/'


def get_templates_directory() -> str:
    return os.path.abspath('../ML_learning/templates') + '/'


def get_logs_directory() -> str:
    return os.path.abspath('../logs') + '/'


def get_log_file_path() -> str:
    return os.path.abspath('../logs/application.log')


def get_price_file_path() -> str:
    return os.path.abspath('../templates/house_price.csv')


def get_png_file_path() -> str:
    return os.path.abspath('../templates') + '/'
