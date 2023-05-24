"""
Author: LL Maepa 44325843

This program will ask the user to input his/her name and display a greeting message, then it will calculate circumference of geometric shapes
"""
import math


user_name = input("Enter your name: ")

print(f"Hello {user_name}\n") #greeting

run = "yes"
while run.lower() == "yes":
    print("\n---For circle---")
    r = float(input("Enter the radius of the circle: "))
    pc = 2*(math.pi)*r #perimeter for circle




    print("\n---For Triangle---")
    a = float(input("Enter size of side 1: "))
    b = float(input("Enter size of side 2: "))
    c = float(input("Enter size of side 3: "))
    ptr = a + b + c #perimeter for triangle

    print("\n---For Square---")

    s= float(input("Enter the size for one side: "))
    ps = 4*s #perimeter for square

    print("\n---For Rectangle---\n")
    l = float(input("Enter the length of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    pr = 2*(l+w) #perimeter for rectangle

    print("\n---Table---")
    #print("%-6s" %"Shape" "%16s"%"Values" "%23s" %"Perimeter" )
    print("%-10s%17s%50s" %(f"Shape","Values","Perimeter"))
    print("%-10s%20s%43.2fcm" %(f"Circle",f"r = {r}cm",pc))
    print("%-10s%40s%23.2fcm" %(f"Triangle",f"a = {a}cm b = {b}cm c = {c}cm",ptr))
    print("%-10s%20s%43.2fcm" %(f"Square",f"s = {s}cm",ps))
    print("%-10s%30s%33.2fcm" %(f"Rectangle",f"l = {l}cm w = {w}cm",pc))
    
    




    run = input(f"{user_name}, Do you wish to start over again?(Yes/No)")
input("Bye!, press enter to exit")


