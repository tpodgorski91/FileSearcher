from pathlib import Path
from typing import List
import subprocess


# def list_drives():
#     system_name = platform.system()
#
#     method = {
#         "Linux": list_drives_linux,
#         "Darwin": list_drives_macos,
#         "Windows": list_drives_macos,
#     }[system_name]
#
#     drives = method()
#     return drives
#
#
# def list_drives_linux() -> List[str]:
#     # TODO: find out how to return
#     return []
#
#
# def list_drives_macos() -> List[str]:
#     import psutil
#     return [
#         partition.device for partition in psutil.disk_partitions()
#     ]
#

# def list_drives_windows() -> List[str]:
#     import string
#     from ctypes import windll
#
#     drives = []
#     bitmask = windll.kernel32.GetLogicalDrives()
#     for letter in string.ascii_uppercase:
#         if bitmask & 1:
#             drives.append(letter)
#         bitmask >>= 1
#
#     return drives

# TODO: return list with index

def list_drives() -> List[str]:
    import psutil
    drives = [
        partition.device for partition in psutil.disk_partitions()
    ]
    for drive in drives:
        print(drive)
    return drives


# TODO: print exact file index from the received list, add header : "index file path"
def get_file(drive, name):
    """
    :param drive:
    :param name:
    :return: print list of files that names are matching with pattern
    """

    file_path = sorted(Path(drive).rglob(f'*{name}*.*'))
    for file in file_path:
        print(file_path.index(file), file)
    # file_path = sorted(Path(f"{drive}").glob(f"*/*{name}*"))
    # file_path = str(file_path)
    # if platform.system() == 'Windows':
    #     file_path = file_path[14:-3]
    # else:
    #     file_path = file_path[11:-3]
    # return file_path


def get_txt_editor():
    import platform
    system_name = platform.system()
    result = {
            "Linux": r'random',
            "Darwin": r'random',
            "Windows": r'notepad.exe',

    }[system_name]
    return result


if __name__ == '__main__':

    list_drives()
    print("Please choose from above one valid drive where text file is stored and type it below."
          "\nChoice should be exactly the same as one from above.")
    user_drive = input()
    print("Please provide either entire or portion of text file name.")
    file_name = input()
    get_file(user_drive, file_name)
    # subprocess.call([get_txt_editor(), get_file(user_drive, file_name)])
