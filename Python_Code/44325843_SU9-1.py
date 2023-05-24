"""
Author: LL Maepa 44325843

This program is a rocks, papers and scissors game, enjoy!!
"""

import random
values = ['Rocks','Papers','Scissors']

print("---Rock, Papers, Scissor")

done = False
played = -1
while done == False:
    value = random.choice(values)
    guess = input("Rocks or Papers or Scissors? or press X to quit: ")
    if guess.lower() == "x":
        done = True
    elif guess.lower() != "rocks" and guess.lower() != "papers" and guess.lower() != 'scissors':
        print('Error, enter only the required words')
    elif guess.lower() == "rocks" and value.lower() == "scissors":
        print(f"You win, I made {value} ")
    elif guess.lower() == "scissors" and value.lower() == "papers":
        print(f"You win, I made {value} ")
    elif guess.lower() == "papers" and value.lower() == "rocks":
        print(f"You win, I made {value}")
    elif guess.lower() == value.lower():
        print("Its a tie")

    else:
        print(f"I win, I made {value}")
    played += 1

print(f"You played {played} times")

    






    