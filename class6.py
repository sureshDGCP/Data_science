# ================================= Nested If else ==================================

#  Note: in the if block its not compulsory to have if-else pair, similarly in main else part also it can be or cant be
# possible to have if-else pair
# Alone If condition can be there instead of else part, it will simply break there and print output

age = int(input("Please mention your age:"))
gender = input("Please mention your gender:")

if age > 45:
    print("You are eligible for Premium class !")
    if gender == "Female":
        print("Special facilities provided")
    # else:
    #     print("No special facilities provided under sr. citizenship")
else:
    print("By default you will be given Normal class.")
    if gender == "Female":
        print("No Special facilities but treated with sweets.")
    else:
        print("No Candies sorry!")



# Reminder for logical operator