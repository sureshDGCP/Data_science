#========================== For Loop =======================

'''
for number in range(0,5):
    print(number)

'''

# for number in range(0,5):             # for number in for loop we need to define the range and provide the start and end point
#     print(number)

# for number in range(5):
#     print(number)

# for number in range(2,5):
#     print(number)

# for number in range(1,5,2):
#     print(number)

# for character in "Suresh":              # when we use for loop on string then it will iterate over each character
#     print(character)

# var2 = "_r_a_v_i_"          # this is solving using for loop
# var3 = len(var2)
# s = ""
# for i in range(1,var3,2):
#     #print(i)
#     s = s + var2[i]
# #    print(var2[i])
# print(s)
#
# print(var2[1:var3:2])       # here we have used the extended slicing to achieve the same thing from above
#
#
# var4 = "waterfall"
# print(var4[1:6:3])
#
#
a = int(input("Enter first no: "))
b = int(input("Enter second no: "))

if True:
    try:
        c = a/b
        print(c)
    except Exception as aa:
        print(f"there is an exception and the exception is {aa}")
        print("There is some issue with passed input please try some other inputs")
    finally:                                          # it will be printed in either case of code whether its running or raising error
        print("This is will be executed compulsory ")

# try:
#     a = int(input("Enter first no: "))
#     b = int(input("Enter second no: "))
#
#     if True:
#         c = a / b
#         print(c)
# except Exception as aa:
#     print(f"there is an exception and the exception is {aa}")
# finally:
#    print("This is finally printed")