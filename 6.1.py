__author__ = 'Topper121'

for row in range(10):

    for j in range(row):
        print (" ",end=" ")

    for j in range(1, 10-row):
        print (j,end=" ")

    print()

for row in range(10):


    print("  " * (10-row), end="")
    for column in range(1, row + 1):
        print(column, end=" ")
    for column in range(row - 1,0,-1):
        print(column, end=" ")
    print()

for row in range(9):

    print(" " * (4+row), end="")
    for j in range(row):
        print ("",end=" ")

    for j in range(1, 9-row):
        print (j,end=" ")

    for k in range(7-row,0,-1):
        print(k, end=" ")
    print()

