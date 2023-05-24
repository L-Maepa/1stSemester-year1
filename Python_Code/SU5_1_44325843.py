#Author = LL Maepa 44325843
#this program will ask the user to input their username and password
#after the user has done that, the program will welcome the user showing their username and password
#it will then ask for the user to input a character and use that character to draw a square

username = input("Enter your username: ") #ask for username
password = input("Enter your password: ") #ask for user password

#print the username and password on a welcome message
print("Welcome " + username + " your password is " + password + "!")
#ask the user to input a character
char = input("Enter a character: ")
#print the character as square
print("Square")
print(char + char + char + char + char + char + char)
print(char + char + char + char + char + char + char)
print(char + char + char + char + char + char + char)
print(char + char + char + char + char + char + char)
