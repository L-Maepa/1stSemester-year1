"""
Author: 44325843 LL Maepa
1. This program will ask the user to enter the character to be converted to ASCII value
2. It will convert the given character to ASCII value and print it
3. Then it will ask the user to enter the ASCII value to be converted to character
4. It will convert and print the resulting character
"""

print("***ASCII and character conversion***\n")

#Converts character to value
char = input("Enter character: ")

outValue = ord(char)

print("The ASCII value is: " + str(outValue) + "\n")

#Converts value to character
value = int(input("Enter the ASCII value: "))

outChar = chr(value)

print("The ASCII character is: " + outChar)


