__author__ = 'Topper121'

# Read in a file from disk and put it in an array.
file = open("super_villains.txt")

name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)

file.close()

print( "There were",len(name_list),"names in the file.")