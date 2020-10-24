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
        "Darwin": list_drives_mac,
        "Windows": list_drives_win,
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


def list_drives_mac() -> List[str]:
    """
    :return: list of user drives on either Windows or macOS
    """
    drives = [
        partition.device for partition in psutil.disk_partitions()
    ]
    return drives


def list_drives_win() -> List[str]:
    import psutil
    """
    :return: list of user drives on either Windows or macOS
    """
    drives = [
        partition.device for partition in psutil.disk_partitions()
    ]
    return drives


def show_drives_list():
    if platform.system() == "Windows" and len(list_drives()) == 1:
        exclude = {'New folder', 'Windows', 'Desktop', 'Program Files', 'Documents and Settings', 'Program Files (x86)',
                   'ProgramData', 'Quarantine', 'Recovery', 'TEMP'}
        for root, dirs, files in os.walk('C:\\', topdown=True):
            dirs[:] = [d for d in dirs if d not in exclude]
            return dirs
    else:
        for drive in list_drives():
            return drive


def file_pattern():
    """
    :return: list of files and search pattern match
    """
    dirname = input("Please choose from above one valid directory where file is stored and type it below."
                        "\nChoice should be exactly the same as one from above.")
    file_name = input("Please provide either entire or portion of file name.")
    if platform.system() == "Windows" and len(list_drives()) == 1:
        result = sorted(Path(f"C:\\{dirname}").rglob(f'*{file_name}*.*'))
    else:
        result = sorted(Path(dirname).rglob(f'*{file_name}*.*'))
    return result


def list_files():
    files_list = []
    for index, file_loc in enumerate(file_pattern()):
        print(index, file_loc)
        file_loc = str(file_loc)
        files_list.append(file_loc)
    if len(files_list) == 0:
        print("Nothing found."
              "\nPlease consider your choice and try again.")
        file_pattern()
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
            print("Index number should equals 0 or higher.\nPlease try again.")
            list_index = int(input("Choose index number corresponding to the file.\n"))
        else:
            open_file_from_list(list_index)
    except IndexError:
        if len(look_for_file) != 0:
            print(f"Incorrect index number selected. Number should be between 0 and {(len(look_for_file)) - 1}"
                    "\nPlease try again.")
        else:
            print("Something went wrong please try again"
                  "\n")
            show_drives_list()
            file_pattern()
        choose_index()
    except ValueError:
        print("Selected index number is not a number."
              "\nPlease try again.")
        choose_index()


if __name__ == '__main__':
    print(show_drives_list())
    look_for_file = list_files()
    choose_index()
