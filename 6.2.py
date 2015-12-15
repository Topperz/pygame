__author__ = 'Topper121'

total = 10

for row in range(9):
    print(total, end=" ")
    total += 1
    for column in range(row):
        print(total, end=" ")
        total += 1
    print()


n = 3
#int(input("Size? "))
n2 = n*2
for row in range(n):
    if row == 0 or row == (n-1):
        print("o" * (n2))
    else:
        print("o", end="")
        print(" " * (n2 - 2), end="")
        print("o")

####################################################


k = int(input("Size? "))
k2 = k*2

for bigrow in range(k2,0,-2):

	for row in range(1,k2,2):
		#print(bigrow)
		if row >= bigrow:
			print(" ", end=" ")
		else:
			print(row, end=" ")
		#prints the row in reverse
		if row == k2-1:
			for rowrev in range(k2-1,0,-2):
				if rowrev >= bigrow:
					print(" ", end=" ")
				else:
					print(rowrev, end=" ")
	print()

for bigrow in range(2,k2+1,2):

	for row in range(1,k2,2):
		#print(bigrow)
		if row >= bigrow:

			print(" ", end=" ")
		else:
			print(row, end=" ")
		#prints the row in reverse
		if row == k2-1:
			for rowrev in range(k2-1,0,-2):
				if rowrev >= bigrow:
					print(" ", end=" ")
				else:
					print(rowrev, end=" ")
	print()


#######################################################

k2 = k*2

#total keeps track of what line is being written, and how many spaces to add.
#When half way though the square, total will start to decrease, to keep the space count accurate.
total=0

for bigrow in range(k2,0,-2):

	for row in range(k2-bigrow+1,k2,2):

		print(row, end=" ")

		#prints the row in reverse
		if row == k2-1:
			print("  "*total*2, end="")
			for rowrev in range(k2-1,0,-2):
				if rowrev >= (total*2)+1:
					print(rowrev, end=" ")
	total += 1
	print()


#The last iteration adds 1 too much to the total value, it is being corrected.
total -= 1

#
for bigrow in range(2,k2+1,2):

	for row in range(k2-bigrow+1,k2,2):

		print(row, end=" ")

		#prints the row in reverse
		if row == k2-1:
			print("  "*total*2, end="")
			for rowrev in range(k2-1,0,-2):
				if rowrev >= (total*2)+1:
					print(rowrev, end=" ")
	total -= 1
	print()