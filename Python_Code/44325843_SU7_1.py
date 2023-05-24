"""
Author: LL Maepa 44325843
This program asks the user for age and gender and checks if the user is age 18 and above and if theyre male or female
"""

ageYrs = int(input("How old are you? "))
gender = input("Are you Female(F) or Male(M), enter only the first letter(M or F): ")


if ageYrs >= 18:
    if gender.lower() == "f" or gender.lower() == "m":
        print("You are eligible to vote")
    else:
        print("Invalid gender")
else:
    print("You are not eligible to vote")