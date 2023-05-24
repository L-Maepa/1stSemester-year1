"""
Author: 44325843 LL Maepa
This program will request the user to input the coefficients a,b and c of the quadratic equation
Then the program will use those coefficients passed on to the variable names a, b and c respectively
The variables will  be used on the quadratic equation to determine the roots
and prints out the roots

"""
import math

print("Solving ax^2 + bx + c = 0")

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

#CALCULATIONS
x1 = round((-abs((b)) + (math.sqrt(b**2-(4*a)*c)))/(2*a),1)
x2 = round((-abs((b)) -(math.sqrt(b**2-(4*a)*c)))/(2*a),1)
print("\n")
print("ROOTS OF GIVEN QUADRATIC EQUATIONS ARE:")

print("x1: " + str(x1))
print("x2: " + str(x2))
