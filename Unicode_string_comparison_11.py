# ========================================== Unicode ============================
"""
computers internally stores characters as numbers, every character has a unique unicode value.

"""

print(ord("a"))
print(ord("A"))

print(ord("*"))
print(ord(" "))
print(ord("9"))
print(ord("0"))

"""
48 to 57 are number digits like 0 to 9 
65 to 90 are capital letters A .... Z 
97 to 122 are small letters a ... z 
rest are special characters 
"""

print(chr(65))
print(chr(3077))
print(chr(2309))

# ====================================== Comparing strings ===========================

print("A"<"B")      # True

print("BAD">"BAT")      # False comparison will be done letter by letter

print("98"<="123")

print("98"<"984")       # greater the length will be greater in value so it will evaluate accordingly.

help("keywords")
#help("return")

# ================== naming conventions =======================

'''
case styles 

camelcase -> totalBill, totalBillAmount
pascalcase ->TotalBill,TotalBillAmount
snakecase ->total_bill,total_bill_amount

'''

# ==================== Rounding Numbers ======================

print(round(3.14,1))
print(round(3.14))

print(0.1+0.2)      # output is 0.30000000000000004 since the float values doesnt store value approximately

# =========================== Compound assignment operator ===============


a = 3
b = 3
a = a + 1
print(a)
b += 1
print(b)

b -= 1
print(b)

b *= 1
print(b)

b /= 2
print(b)

# =========================== Floor Divison ==============================

print(3/2)
print(3//2)  # when we want only integral part of devision use floor devision


a = (3/2)
print(type(a))      #<class 'float'>

b = (3//2)
print(type(b))      # <class 'int'>

print("suresh"=="Suresh")   # its doing comparison


# ==================  Escape  characters =================================

print("Hello "
      "world")

print("Hello\nworld")       # new line

print("Hello\tworld")       #tab space


#print('It's python')       #this will create an error since we are using single quotation inside and outside

print("It's Python")
print('It\'s Python')           # use the back slash to eliminate the special feature of characters and considers it as string.


print("Hello\World")
print('Hello\World')
print("Hello\\World")







