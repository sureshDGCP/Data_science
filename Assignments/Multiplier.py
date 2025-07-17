'''
Question 3: Take 2 inputs from user a, b, and find out "b" multiplier of "a"
if then print its multiplier if not then print.
--done
'''


var1 = input("please give 1st no:")
var2 = input("please give 2nd no:")

if (int(var2) % int(var1)) == 0:
    print(f"{var2} is multiplier of {var1}")
else:
    print(f"{var2} is not a multiplier of {var1}")