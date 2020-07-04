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


def get_file():

    drive_name, file_name = user_input()
    files_list = []
    file_path = sorted(Path(drive_name).rglob(f'*{file_name}*.*'))
    for file_loc in file_path:
        print(file_path.index(file_loc), file_loc)
        file_loc = str(file_loc)
        files_list.append(file_loc)
    if len(files_list) == 0:
        print("Nothing found."
              "\nPlease consider your choice and try again.")
        list_drives()
        get_file()
    else:
        try:
            print("Choose index.")
            list_index = int(input())
            if platform.system() == "Windows":
                os.startfile(file_path[list_index])
            elif platform.system() == "Darwin":
                subprocess.Popen(["open", file_path[list_index]])
            else:
                subprocess.Popen(["xdg-open", file_path[list_index]])
            return file_path[list_index]
        except IndexError:
            print("Index out of scope."
                  "\nPlease try again.")
# TODO: maybe create choose_index function to enable choosing option again


def user_input():
    print("Please choose from above one valid drive where text file is stored and type it below."
          "\nChoice should be exactly the same as one from above.")
    drive_name = input()
    print("Please provide either entire or portion of text file name.")
    file_name = input()
    return drive_name, file_name


# def choose_index():
#     print("Choose index.")
#     list_index = int(input())
#     if platform.system() == "Windows":
#         os.startfile(file_path[list_index])
#     elif platform.system() == "Darwin":
#         subprocess.Popen(["open", file_path[list_index]])
#     else:
#         subprocess.Popen(["xdg-open", file_path[list_index]])
#     return file_path[list_index]


if __name__ == '__main__':

    list_drives()
    get_file()

