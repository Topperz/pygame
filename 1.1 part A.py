__author__ = 'Topper121'

temp_in_fahrenheit = input("Enter temperature in Fahrenheit:")
#convert temp to float
temp_in_fahrenheit = float(temp_in_fahrenheit)

#calculate temp in celcius from farenheit
temp_in_celcius = (temp_in_fahrenheit - 32) / 1.8

print("The temperature in celcius is: ", temp_in_celcius)