import os.path
from pathlib import Path
import yaml

path = Path(__file__).parent
with open(str(path) + '/config.yml') as yml:
    config_local = yaml.safe_load(yml)


def config_initialize():
    path = Path(__file__).parent
    with open(str(path) + '/config.yml') as yml:
        config_init = yaml.safe_load(yml)

    return config_init


def get_backup_directory() -> str:
    return os.path.abspath('../../templates/backup') + '/'


def get_templates_directory() -> str:
    return os.path.abspath('../../templates') + '/'


def get_logs_directory() -> str:
    return os.path.abspath('../utils/logs') + '/'


def get_log_file_path() -> str:
    return os.path.abspath('../utils/logs/application.log')


def get_price_file_path() -> str:
    return os.path.abspath('') + config_local['DIRECTORY']['ML_LEARNING_BASE_DIR'] + '/templates/house_price.csv'


def get_png_file_path() -> str:
    return os.path.abspath('') + config_local['DIRECTORY']['ML_LEARNING_BASE_DIR'] + '/output/'
