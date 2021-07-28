import os.path
from pathlib import Path
import yaml

# 清書予定

path = Path(__file__).parent
with open(str(path) + '/config.yml') as yml:
    config = yaml.safe_load(yml)


def config_initialize():
    path = Path(__file__).parent
    with open(str(path) + '/config.yml') as yml:
        config = yaml.safe_load(yml)

    return config


def get_backup_directory() -> str:
    return os.path.abspath('./') + '/applications' + config['DIRECTORY']['ML_LEARNING_BASE_DIR'] + 'templates/backup/'


def get_templates_directory() -> str:
    return os.path.abspath('./') + '/applications' + config['DIRECTORY']['ML_LEARNING_BASE_DIR'] + 'templates/'


def get_logs_directory() -> str:
    return os.path.abspath('../utils/logs') + '/'


def get_log_file_path() -> str:
    return os.path.abspath('../utils/logs/application.log')


def get_price_file_path() -> str:
    return os.path.abspath('') + config['DIRECTORY']['SCRAPE_BASE_DIR'] + '/templates/house_price.csv'


def get_png_file_path() -> str:
    return os.path.abspath('') + config['DIRECTORY']['ML_LEARNING_BASE_DIR'] + '/output/'
