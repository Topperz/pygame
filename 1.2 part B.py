__author__ = 'Topper121'

print("Calculator for area of trapezoid")

height = float(input("Enter the height of the trapezoid:"))
length_bottom = float(input("Enter the length of the bottom base:"))
length_top = float(input("Enter the length of the top base:"))

trap_area = 1/2 * (length_bottom + length_top) * height

print("The area is: ", trap_area)