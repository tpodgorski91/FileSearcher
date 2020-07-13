from pathlib import Path
from typing import List
import platform
import os
import subprocess


def list_drives():
    system_name = platform.system()
    method = {
        "Linux": list_drives_linux,
        "Darwin": list_drives_win_mac,
        "Windows": list_drives_win_mac,
    }[system_name]
    drives = method()
    return drives


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
    print("Please choose from above one valid drive where file is stored and type it below."
          "\nChoice should be exactly the same as one from above.")
    drive_name = input()
    print("Please provide either entire or portion of file name.")
    file_name = input()
    files_list = []
    # print(drive_name, file_name)
    file_path = sorted(Path(drive_name).rglob(f'*{file_name}*.*'))
    for file_loc in file_path:
        print(file_path.index(file_loc), file_loc)
        file_loc = str(file_loc)
        files_list.append(file_loc)
    if len(files_list) == 0:
        print("Nothing found."
              "\nPlease consider your choice and try again.")
        user_input()
    return files_list


def choose_index():
    # TODO: how to avoid when user input is negative number
    """

    :return: opens chosen file from the list base on list index
    """
    try:
        print("Choose index number corresponding to the file.")
        # print(look_for_file)
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

#does
