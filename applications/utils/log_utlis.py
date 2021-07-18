import logging
import logging.config
import os

#
# class ApplicationLog():
#     def __init__(self):
#         formatter = '%(asctime)s:%(message)s'
#         logging.basicConfig(filename='application.log', encoding='utf-8', level=logging.DEBUG, format=formatter)
#
#     def write_log(self):
#         logger = logging.getLogger(__name__)
#         logger.info('from logutil')

def write_log(data):
    formatter = '%(asctime)s:%(message)s'
    logging.basicConfig(filename='application.log', encoding='utf-8', level=logging.INFO, format=formatter)
    logging.info(data)
    # logger = logging.getLogger(__name__)
    # logger.info(data)


    # myname = os.path.basename()
write_log('test')