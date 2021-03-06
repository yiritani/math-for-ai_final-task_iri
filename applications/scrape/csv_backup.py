import os
import datetime
import glob
import shutil
from .config import config_getter

config = config_getter.config_initialize()
resource_filename = config['FILE']['BACKUP_FILE_NAME']
MAX_FILES = 2


def backup_csv_file() -> None:
    """
    Csv backup to 3 generations
    :return: None
    """
    now = datetime.datetime.now()

    templates_path = config_getter.get_templates_directory()
    backup_path = config_getter.get_backup_directory()

    filename_timestamp = now.strftime('%Y%m%d%H%M%S')

    backup_file_full_path = backup_path + resource_filename + '_' + filename_timestamp

    file_list = glob.glob(backup_path + "*")

    sorted(file_list, key=lambda f: os.stat(f).st_mtime, reverse=False)

    if len(file_list) > MAX_FILES:
        del_num = len(file_list) - MAX_FILES
        for i in range(del_num):
            os.remove(file_list[i])

    shutil.copy(str(templates_path) + resource_filename, backup_file_full_path)
    # logger.info('from backup')
