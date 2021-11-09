import logging
import inspect
import os
from datetime import datetime


class Logger():
    def __init__(self):
        filename = 'log/{:%Y-%m-%d}.log'.format(datetime.now())
        logging.basicConfig(level=logging.DEBUG,
                            format="[%(asctime)s] [%(process)d] [%(name)s] [%(levelname)s] %(message)s",
                            filename=filename
                            )

    def debug(self, execution_location, log_message):
        self.logger = logging.getLogger(execution_location)
        self.logger.debug(log_message)

    def info(self, execution_location, log_message):
        self.logger = logging.getLogger(execution_location)
        self.logger.info(log_message)

    def warning(self, execution_location, log_message):
        self.logger = logging.getLogger(execution_location)
        self.logger.warning(log_message)

    def error(self, execution_location, log_message):
        self.logger = logging.getLogger(execution_location)
        self.logger.error(log_message)


class Trace():
    @classmethod
    def execution_location(self):
        frame = inspect.currentframe().f_back
        return "{}:{} {}".format(os.path.basename(frame.f_code.co_filename), frame.f_lineno, frame.f_code.co_name)
