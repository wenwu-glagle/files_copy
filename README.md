# files_copy
copy files wintin file-list file, the file name is not necessary to be comleted, just be substring of origin filename is ok.

## Usage

<pre>
python3 -m fcp -h
usage: fcp [-f FILE...] [-s SRC] [-d DST] [-sc | -dc] [-p] [-m] [-e FILE...]] [-l] [-h]

Copy files with given name in the input file from a directory and its
subfolders to another directory. A destination folder must be outside of a
source folder.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE [FILE ...], --file FILE [FILE ...]
                        one or more files which be written with file list,
                        enter with txt, separate by spaces
  -s SRC, --source SRC  source folder path
  -d DST, --dest DST    destination folder path
  -sc, --srccwd         use current working directory as a source
  -dc, --dstcwd         use current working directory as a destination
  -p, --preserve        preserve source folder structure
  -m, --move            move files instead of copying
  -e FILE [FILE ...], --exclude FILE [FILE ...]
                        exclude files which be written with file list from
                        processing
  -l, --log             create and save log to the destination folder
</pre>

## Test case:  

python3 -m fcp -f ~/code/PycharmProjects/Files_Copy/test/file_list_test.txt -s ~/code/PycharmProjects/Files_Copy/test/ -d ~/code/test/

Copying 2 files are listed in /home/sww/code/PycharmProjects/Files_Copy/test/file_list_test.txt file from /home/sww/code/PycharmProjects/Files_Copy/test to /home/sww/code/test
Progress: |===================================================================================================================================================================| 100% Done


## Known issue:
- Do not support relative path

## Todo:
- Support large file list
- Support copy recursive
- Support --exclud optione
- Support --invert option

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Reference

[selective_copy](https://github.com/pltnk/selective_copy)

