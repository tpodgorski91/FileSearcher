from pathlib import Path
from typing import List
import platform
import os
import subprocess


def list_drives() -> List[str]:
    import psutil
    drives = [
        partition.device for partition in psutil.disk_partitions()
    ]
    for drive in drives:
        print(drive)
    return drives


def get_file(drive, name):
    """
    :param drive:
    :param name:
    :return: print list of files that names are matching with pattern
    """
    files_list = []
    file_path = sorted(Path(drive).rglob(f'*{name}*.*'))
    for file_loc in file_path:
        print(file_path.index(file_loc), file_loc)
        file_loc = str(file_loc)
        files_list.append(file_loc)
    print("Choose index.")
    list_index = int(input())
    if platform.system() == "Windows":
        os.startfile(file_path[list_index])
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", file_path[list_index]])
    else:
        subprocess.Popen(["xdg-open", file_path[list_index]])
    return file_path[list_index]


if __name__ == '__main__':

    list_drives()
    print("Please choose from above one valid drive where text file is stored and type it below."
          "\nChoice should be exactly the same as one from above.")
    user_drive = input()
    print("Please provide either entire or portion of text file name.")
    file_name = input()
    get_file(user_drive, file_name)
