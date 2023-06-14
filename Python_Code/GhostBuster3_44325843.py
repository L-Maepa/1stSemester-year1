"""
Author: LL Maepa 44325843

This program will ask the user to enter a secret value in range given and ask the user to guide if the value guessed by the program is smaller or larger than their secret value
"""

import random
import time

tries = 0
correct = False


prompt = int(input("Player, enter a secret value in the range 1-100: "))

entryTime = time.time()

while correct is not True:
    
    tries += 1
    finalTime = time.time()
    guess = random.randint(0,100)
    
    guidance = int(input("Guidance is necessary; is the guess larger (1), or smaller (0) than your secret value? "))
    
    
    doneTime = finalTime - entryTime #the final time recorded minus the entry time will give us the time lapse
    doneTime = round(doneTime,2)
    
    if (guess > prompt and guidance == 0) or (guess < prompt and guidance == 1):#I try to use less lines of code by including the "and/or"
        print(f"The guess number is {guess}")
        print("Oops, you got that one wrong")
    elif (guess > prompt and guidance== 1) or (guess < prompt and guidance == 0):
        print(f"The guess number is {guess}")
        print("You got it right!!!")
        print(f"It took you {tries} tries to guess your secret value")
        print(f"The time lapse is {doneTime} seconds.")
        correct = True
    else:#This is when the user has entered a guidance value of any number except 0 and 1
        print("Error: Enter a guidance value of 1 or 0!")
        tries += -1 #this will reduce the tries count by 1 because it has incremented and the user entered a value outside the required ones and does not count as a try
