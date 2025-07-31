"""
Question 7: Electricity bill calculator
take input from user no of units used and if it is 0 - 100 we will charge 1.5 rs per unit
if its 100 to 200 units then it will be 2 rs per units
if at all above 200 units then its 3rs per unit

(use tax like computation for this use case)

"""


units = int(input("Enter no of units utilised by you:"))

if units in range(0,100):
    charge1 = units * 1.5
    print(charge1)
elif units in range(100,200):
    units = (units - 100)

