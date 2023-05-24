"""
Author: LL Maepa 44325843

This program will use the for loop to display the number that the user will provide and the following descending numbers.

"""

no1 = int(input("Enter a postive integer: "))

if no1 > 0:
    for i in range((no1-1), -1, -1):
        print(i, end=" ")

    input("\nPress enter to exit...")
else:
    print("Number must be positive")
    input("Press enter to exit")