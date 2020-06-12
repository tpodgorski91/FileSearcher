import string
from ctypes import windll
from pathlib import Path, PurePath


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives


if __name__ == '__main__':
    for element in get_drives():
        print(element)    # On my PC, this prints ['A', 'C', 'D', 'F', 'H']
    print("")
    print("Please type drive letter from the list above (e.g. D)")
    user_driver = input()
    print("Please provide file name")
    file_name = input()
    p = sorted(Path(f"{user_driver}:/").glob(f"*/*{file_name}*.txt"))
    f = open(p[0])
    print(f.read())