import os, glob
#to find multiple amount of files

files = glob.glob(r'D:\*\*.txt')

for file in range(len(files)):
	print(str(file)+ " " + files[file])

print("Plz enter file number from the list above")
numer = int(input())
if numer > len(files):
    print("Plz enter number equal to/ lower than " + str(len(files)-1))
tekst = open(files[numer],"r")
content = tekst.read()
print(content)

