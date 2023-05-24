"""
Author: 44325843 LL Maepa
This program will ask the user for the base, length and height of the triangular prism
Then it will calculate the area and volume
Then it will use the volume to determine the width
after determining the width it will calculate the space diagonal 
Then it will print out the results to the user
"""

import math

print("Cuboid calculator")
print("\n")

b = round(float(input("Enter the base(cm): ")),1)
l = round(float(input("Enter the length(cm): ")),1)
h = round(float(input("Enter the height(cm): ")),1)

#Calculations

area = round(b*l + l*h + b*h + h*math.sqrt(math.exp2(l)+math.exp2(b)),4)
volume = round((l*b*h)/2,2)
w = b
spaceD = round(math.sqrt(math.exp2(l)+math.exp2(w)+math.exp2(h)),3)

print("\n")
print("Area of the triangular prism is " + str(area) + " square cm \
    \nSpace diagonal of the triangular prism is " + str(spaceD) + " cm \
        \nVolume of the triangular prism is " + str(volume) + " cubic cm")
print("\n")
print("**Triangular prism dimensions:** \n\
    base = " + str(b) + " cm" + " "*2 + "length = " + str(l) + " cm" + " \t height = " + str(h) + " cm")
