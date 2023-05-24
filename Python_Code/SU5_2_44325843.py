#Author = LL Maepa 44325843
# This program will  ask the user to enter the length and width of surface area(rectangle) that needs to be calculated in cm

print("Concatenated values")
# ask the user to input length and width of the rectangle to concatenate
length = str(input("Enter length for the rectangle: "))
width = str(input("Enter width for the rectangle: "))

#print the concatenated value 
print("Result: " + length + width)

#ask the user to input the length and width of the rectangle, now to calculate
print("Values to calculate area and parimeter")
lengthc =  int(input("Enter length for the rectangle: "))
widthc = int(input("Enter width for the rectangle: "))

#the calculations
area = lengthc * widthc # multiply the length with width

#calculating perimeter by multiplying the sum of length and width by 2
perimeter = 2*(lengthc + widthc) 

 

#printing the values
print("Area: " + str(area))
print("Perimeter: " + str(perimeter))
