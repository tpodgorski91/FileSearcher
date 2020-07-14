import os
import platform
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
    import psutil
    drives = [
        partition.mountpoint for partition in psutil.disk_partitions()
    ]
    for drive in drives:
        print(drive)
    return drives


def list_drives_win_mac() -> List[str]:
    """
    :return: list of user drives on either Windows or macOS
    """
    import psutil
    drives = [
        partition.device for partition in psutil.disk_partitions()
    ]
    for drive in drives:
        print(drive)
    return drives


def user_input():
    """
    :return: list of files and search pattern match
    """
    msg1 = "Please choose from above one valid drive where file is stored and type it below."
            "\nChoice should be exactly the same as one from above."
    drive_name = input(msg1)
    msg2 = "Please provide either entire or portion of file name."
    file_name = input(msg2)
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


def choose_index():
    """
    :return: opens chosen file from the list base on list index
    """
    try:
        print("Choose index number corresponding to the file.")
        list_index = int(input())
        print(look_for_file[list_index])
        if platform.system() == "Windows":
            os.startfile(look_for_file[list_index])
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", look_for_file[list_index]])
        else:
            subprocess.Popen(["xdg-open", look_for_file[list_index]])
        return look_for_file[list_index]
    except IndexError:
        print(f"Incorrect index number selected. Number should be between 0 and {(len(look_for_file))- 1}"
              "\nPlease try again."
              "\n")

        choose_index()
    except ValueError:
        print("Selected index number is not a number."
              "\nPlease try again."
              "\n")
        choose_index()


if __name__ == '__main__':
    list_drives()
    look_for_file = user_input()
    choose_index()

# dub dub