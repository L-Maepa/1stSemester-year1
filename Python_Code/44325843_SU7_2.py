"""
Author: LL Maepa 44325843
This program will act as a calculator, it will prompt the user to enter two numbers and an operator
and display the answer or the errors if it encounters one
"""

numOne = int(input("Enter a number: "))
operator = input("Enter an operator: ")
numTwo = int(input("Enter a number: "))

if operator == "/" and numTwo >0:
    result = numOne/numTwo
    print(result)
elif operator == "/" and numTwo == 0:
    print("Error: Division by zero!!")
elif operator == "+":
    result = numOne + numTwo
    print(result)
elif operator == "-":
    result = numOne - numTwo
    print(result)
else:
    print("Error:You entered an invalid operator!!")

