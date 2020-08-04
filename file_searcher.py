import os
import platform
import psutil
import subprocess
from pathlib import Path
from typing import List


def list_drives():
    system_name = platform.system()
    method = {
        "Linux": list_drives_linux,
        "Darwin": list_drives_win_mac,
        "Windows": list_drives_win_mac,
    }[system_name]
    return method()


def list_drives_linux() -> List[str]:
    """
    :return: list of user drives on Linux
    """
    drives = [
        partition.mountpoint for partition in psutil.disk_partitions()
    ]
    return drives


def list_drives_win_mac() -> List[str]:
    """
    :return: list of user drives on either Windows or macOS
    """
    drives = [
        partition.device for partition in psutil.disk_partitions()
    ]
    return drives


def show_drives_list():
    for drive in list_drives():
        print(drive)


def user_input():
    """
    :return: list of files and search pattern match
    """
    drive_name = input("Please choose from above one valid drive where file is stored and type it below."
            "\nChoice should be exactly the same as one from above.")
    file_name = input("Please provide either entire or portion of file name.")
    files_list = []
    file_path = sorted(Path(drive_name).rglob(f'*{file_name}*.*'))
    for index, file_loc in enumerate(file_path):
        print(index, file_loc)
        file_loc = str(file_loc)
        files_list.append(file_loc)
    if len(files_list) == 0:
        print("Nothing found."
              "\nPlease consider your choice and try again.")
        user_input()
    return files_list


def open_file_from_list(index):
    if platform.system() == "Windows":
        os.startfile(look_for_file[index])
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", look_for_file[index]])
    else:
        subprocess.Popen(["xdg-open", look_for_file[index]])


def choose_index():
    """
    :return: opens chosen file from the list base on list index
    """
    try:
        list_index = int(input("Choose index number corresponding to the file.\n"))
        while list_index < 0:
            print("Index number should equals 0 or higher."
                  "\nPlease try again.")
            list_index = int(input("Choose index number corresponding to the file.\n"))
        else:
            open_file_from_list(list_index)
    except IndexError:
        print(f"Incorrect index number selected. Number should be between 0 and {(len(look_for_file)) - 1}"
              "\nPlease try again.")
    except ValueError:
        print("Selected index number is not a number."
              "\nPlease try again.")
    choose_index()


if __name__ == '__main__':
    show_drives_list()
    user_input()
    choose_index()
    
