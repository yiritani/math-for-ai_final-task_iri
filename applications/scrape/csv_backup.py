import csv
import logging
import os
import datetime
import glob
import shutil
from pathlib import Path

import yaml

from applications.utils.log_utlis import write_log

path = Path(__file__).parent
with open(str(path) + '/config.yml') as yml:
    config = yaml.load(yml)
resource_filename = config['BACKUP_FILE_NAME']
max_file = 2

# logger = logging.getLogger(__name__)
# h = logging.FileHandler('csv_backup.log')
# logger.addHandler(h)


def backupCsvFile():
    global path
    path /= '../ML_learning/templates/'
    backup_path = str(path) + '/backup/'

    now = datetime.datetime.now()
    filename_timestamp = now.strftime('%Y%m%d%H%M%S')

    backup_file_full_path = backup_path + resource_filename + '_' + filename_timestamp

    file_list = glob.glob(backup_path + "*")

    sorted(file_list, key=lambda f: os.stat(f).st_mtime, reverse=False)

    if len(file_list) > int(max_file):
        del_num = len(file_list) - int(max_file)
        for i in range(del_num):
            os.remove(file_list[i])

    shutil.copy(str(path) + '/' + resource_filename, backup_file_full_path)
    # logger.info('from backup')


if __name__ == '__main__':
    backupCsvFile()
    # write_log('aaa')
    # print(__name__)
    # log_util = ApplicationLog()
    # log_util.write_log()
