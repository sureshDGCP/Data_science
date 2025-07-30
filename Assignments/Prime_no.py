'''
Question 4: take an input from user and identify its a prime no or not
and then print

'''

var1 = input("Please enter a number to check whether its a Prime no or not :")
#print(var1)

flag = False

if int(var1) == 0 or int(var1) == 1:
    print(f"The given no {var1} is not a Prime no:")
elif int(var1) > 1:
    for i in range(2, int(var1)):
        if (int(var1) % i) == 0:
            print(f"Factor found")
            flag = True

    if flag == True:
        print(f"The provided no is not Prime no.")
    else:
        print(f"The provided no is Prime no.")



# if (int(var1) % int(var1)) == 1 and (int(var1) % int(var1)) == int(var1):
#     print("Its a Prime number !")
# else:
#     print("Its not a Prime number")

#we need to iterate through no from 1 to square root of given no.
#Divisor = (Dividend - Remainder) ÷ Quotient

