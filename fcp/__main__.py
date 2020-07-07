# -*- coding:utf-8 -*-
# @ProjectName :Files_Copy
# @FileName    :__main__.py
# @Time        :2020/7/4 下午2:55
# @Author      :sww

from fcp.cli import MyArgParser
from fcp.process import MyHandler


def main():
    """Process files according to the command line arguments."""
    parser = MyArgParser()
    handler = MyHandler(parser.args)
    print(handler.message)
    handler.log.logger.info(handler.message)
    handler.process()
    handler.log.logger.info(f"Process finished\n")
    handler.log.close()


if __name__ == "__main__":
    main()
