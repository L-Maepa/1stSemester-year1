"""
Author: LL Maepa 44325843

Multiplication table from 1 to 12 and the sum of the totals
"""

#Ask user to enter the a correct value
error = True
while error == True:
    number = int(input("Enter an integer: "))
    if number > 0:
        error = False
    else:
        error = True


totals = []


#LOOP FOR MULTIPLICATION TABLE
print("---Multiplication Table---")
for x in range(1,13):
    value = x * number
    totals.append(value)
    print(f"{x} x {number} = {value}")


#SUM OF THE TOTALS
print("---Sum of totals---")

totalSum = sum(totals)
for total in totals:
    if total/len(totals) == number:
        print(total, end= " = ")
    else:
        print(total, end=" + ")
print(totalSum)
