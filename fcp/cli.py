# -*- coding:utf-8 -*-
# @ProjectName :Files_Copy
# @FileName    :cli.py
# @Time        :2020/7/4 下午2:51
# @Author      :sww


import os
from argparse import ArgumentParser


class MyArgParser:
    """Command line arguments parser."""
    def __init__(self):
        """Parse command line arguments, format given extensions and arguments containing paths."""
        self.parser = ArgumentParser(
            usage="fcp [-f FILE...] [-s SRC] [-d DST] [-sc | -dc] "
                  "[-p] [-m] [-e FILE...]] [-l] [-h]",
            description="Copy files with given name in the input file from a directory and its subfolders "
                        "to another directory. "
                        "A destination folder must be outside of a source folder.",
        )
        self.parser.add_argument(
            "-f",
            "--file",
            required=True,
            nargs="+",
            help="one or more files which be written with file list, enter with txt, separate by spaces",
        )
        self.parser.add_argument(
            "-s",
            "--source",
            help="source folder path", metavar="SRC"
        )
        self.parser.add_argument(
            "-d",
            "--dest",
            help="destination folder path", metavar="DST"
        )
        group = self.parser.add_mutually_exclusive_group()
        group.add_argument(
            "-sc",
            "--srccwd",
            action="store_true",
            help="use current working directory as a source",
        )
        group.add_argument(
            "-dc",
            "--dstcwd",
            action="store_true",
            help="use current working directory as a destination",
        )
        self.parser.add_argument(
            "-p",
            "--preserve",
            action="store_true",
            help="preserve source folder structure",
        )
        self.parser.add_argument(
            "-m",
            "--move",
            action="store_true",
            help="move files instead of copying"
        )
        self.parser.add_argument(
            "-e",
            "--exclude",
            nargs="+",
            help="exclude files which be written with file list from processing",
            metavar="FILE",
        )
        self.parser.add_argument(
            "-l",
            "--log",
            action="store_true",
            help="create and save log to the destination folder",
        )
        self.args = self.parser.parse_args()
        self.args.file = tuple(set(f"{item}" for item in self.args.file))
        if self.args.source:
            self.args.source = os.path.normpath(self.args.source.strip())
        if self.args.dest:
            self.args.dest = os.path.normpath(self.args.dest.strip())
        self.args.exclude = (
            tuple(set(f"{item}" for item in self.args.exclude)) if self.args.exclude else tuple()
        )


if __name__ == "__main__":
    run_code = 0
