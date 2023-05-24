"""
Author: LL Maepa 44325843

This program will use the while loop to display the integer the user entered and the numbers before it in ascending it
and also add all those numbers and display the sum
"""

nodis = int(input("Enter a postive integer: "))

n = 0
su = 0

if nodis > 0:
    while n < nodis:
        print(n, end=" ")
        n += 1
        su += n
    su -= nodis
    print("\n")
    n = 0
    while n < nodis:
        if ((nodis-1)-n) == 0: #for example, if user gave us 5 then, 5-1=4 which is the last value to be displayed from the loop
            print(n, end=" = ")
        else:
            print(n, end=" + ")
        n += 1
    print(su)
    input("Press enter to exit")

    
else:
    print("Number must be positive")
    input("Press enter to exit")




    


