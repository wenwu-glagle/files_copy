# -*- coding:utf-8 -*-
# @ProjectName :Files_Copy
# @FileName    :log.py
# @Time        :2020/7/5 下午3:34
# @Author      :sww

import logging
import os


class Log:
    """Logging handler."""

    def __init__(self, args, destination):
        """
        Create logger instance and slcp.log file
        in the destination folder if logging is turned on
        in command line arguments. If not create only logger instance.
        :param args: argparse.Namespace. Command line arguments.
        :param destination: str. Destination folder path.
        """
        self.logger = logging.getLogger("slcp")
        self.logger.setLevel(logging.CRITICAL)
        self.log = args.log
        if self.log:
            self.logger.setLevel(logging.INFO)
            fh = logging.FileHandler(
                os.path.join(destination, "slcp.log"), encoding="utf-8"
            )
            formatter = logging.Formatter(
                "%(asctime)s %(message)s", "%d.%m.%Y %H:%M:%S"
            )
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

    def close(self):
        """
        Close selective_copy.log file and remove it from logger
        file handlers if logging is turned on in command line arguments.
        :return: NoneType.
        """
        if self.log:
            self.logger.handlers[0].close()
            self.logger.handlers = []


if __name__ == "__main__":
    run_code = 0
