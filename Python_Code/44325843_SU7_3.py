"""
Author: LL Maepa 44325843
This program will ask the user to enter the base and an exponent and check if both base and exponent
are greater than 0, the it will use pow() function to calculate.
"""
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

if base == 0 and exponent == 0:
    print("Error! indefinite form(0^0)")
elif exponent < 0:
    print("Error: exponent cannot be negative!")
else:
    result = pow(base,exponent)
    print(result)