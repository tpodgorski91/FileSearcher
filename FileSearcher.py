import glob
#TODO open file in another application e.g. Notepad
#TODO print out only file name without path
#TODO make list of files more readable

print("Enter file name")
filename = input()

files = glob.glob("D:\\*\\" + filename + "*")

for file in range(len(files)):
    print(str(file) + "  " + files[file])

print("Plz enter file number from the list above")
number = int(input())
if number > len(files):
    print("Plz enter number equal to/ lower than " + str(len(files)-1))
tekst = open(files[number],"r")
content = tekst.read()
print(content)

