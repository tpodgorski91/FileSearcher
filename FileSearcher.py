import glob, subprocess

#TODO: run program automatically

files=[]
while not files:
    print("Please enter txt file name")
    filename = input()
    files = glob.glob("D:\\*\\*" + filename + "*.txt")

for file in range(len(files)):
    print(str(file) + "  " + files[file])

print("Please enter row index")
number = int(input())

try:
    while number < 0 or number > len(files)-1:
        print("Plz enter index no higher than " + str(len(files) - 1))
        number = int(input())
except IndexError:
    print("Index is out of range")

subprocess.call([r"notepad.exe", files[number]])