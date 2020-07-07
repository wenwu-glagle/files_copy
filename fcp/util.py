# -*- coding:utf-8 -*-
# @ProjectName :Files_Copy
# @FileName    :util.py
# @Time        :2020/7/5 上午11:54
# @Author      :sww

from accepts import accepts
import re
import codecs
import os.path
import shutil


@accepts(str, str, bool)
def is_substr_match(string, substring, total_match=False):
    """
    match substring with string, using regex match in fuzzy match.
    when total_match is False, use fuzzy match.
    :param total_match:
    :param substring: need to match,
    :param string : source string

    :return: True   match success
             False  match failed
    """
    if total_match:
        if string == substring:
            return True
        else:
            return False
    else:
        sub_str_reg = re.compile(substring)
        match = re.search(sub_str_reg, string)
        if match:
            return True

    return False


@accepts(tuple)
def pre_deal_file_list(files):
    """
    pre deal file list
    including duplicate removal and sort
    Todo: large file list
    :return: None
    """
    for file in files:
        if file.endswith('txt'):

            # back up file first
            back_up_file = 'back_up_' + os.path.basename(file)
            if not os.path.exists(back_up_file):
                try:
                    shutil.copy(file, back_up_file)
                except IOError as e:
                    print("Unable to copy file. %s" % e)

            result = []
            with codecs.open(file, 'r', 'utf8') as f:
                for line in f:
                    if line.strip():
                        line = line.strip()
                        if line not in result:
                            result.append(line)
                        else:
                            continue
                    else:
                        continue

            result.sort()

            with codecs.open(file, 'w', 'utf8') as f:
                for line in result:
                    print(line)
                    f.write(line + '\n')


if __name__ == "__main__":
    run_code = 0
