# =============== Type Conversion ========================

print(type(10))     #<class 'int'>
print(type(4.2))    #<class 'float'>
print(type("hi"))   #<class 'str'>
print(type(True))   #<class 'bool'>


var1 = "556"    # whaterver we define in quote it will consiered as srting
print(type(var1))       #<class 'str'>

# converting the above variable value into integer

var1 = int(var1)    # for converting into int use the int keyword
var2 = "five"
# var2 = int(var2)
# print(type(var2))   #ValueError: invalid literal for int() with base 10: 'five'

# Note : int() converts valid data of any type into integer

var3 = "5.0"
print(type(var3))
# var3 = int(var3)        #ValueError: invalid literal for int() with base 10: '5.0'

# Note :

# int() -> converts to integer datatypes
# float() -> converts to float datatypes
# str() -> converts to string datatypes
# bool() -> converts to boolean datatypes

# ======================= Relational Operators ====================
"""
Relational operators [ > , <, ==(is equal to), != (is  not equal to), >=, <= ]
it always gives boolean as output
e.g."""
print(5 < 10)   #True

print("ABC"=="abc") #False since Python is case sensitive caps and small letters are not same in pyhton


# ====================== other operators =============================
#
# [% -> remainder operator, ** -> exponent operator like


print(6%3)  #  -> 0
print(5%2)  # -> 1
a = 2
b= 4
print(a**b)     # 16
print(2**4)     # 16

# ========================== conditional programming ============================

'''
If, else , elif  

syntax is 
if condition:                        ( if this condition is true ...) then run block of other code or else part 
    block of code                    ( whatever you will define in this block of code it will belong to if condition)     

'''

if True:
    print("Hi Sreeja")

# if True:
#     print("Hi Sreeja")
# #      print("Hi Suresh")              # IndentationError: unexpected indent

'''
if condition:
    block of code
else:
    block of code

'''
a = 10
if a > 5:
    print("This is bigger no.")
else:
    print("This is smaller no.")


var1 = int(input("Pleae provide a number"))
#var1 = int(var1)
if var1 > 0:
    print("Its a positive no")
elif var1 < 0:
    print("Its a Negative no")
else:
    print("Its a number zero")




