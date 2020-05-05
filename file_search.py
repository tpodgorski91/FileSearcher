import os
import glob


def file_direction():
    print("Please enter file name")
    file_name = input()
    print(os.getcwd())
    print("Please enter direction where look for")
    required_dir = input()
    os.chdir("D:\\*\\*")
    string = f"{required_dir}:\\{file_name}*.txt"
    print(string)
    # TODO: glob returns pathname, is this really what I am looking for? Main is to open correct file
    # TODO: can I use regex to find file in specific folder?
    whole_direction = glob.glob(f'./{file_name}*.txt')

    print(whole_direction)


file_direction()
