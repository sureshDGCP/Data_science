""" =============================  String Methods =================================== """
from time import process_time

'''
They are inbuilt reusable methods. 

e.g. isdigit(), lower(), upper(), startwith(), endswith(), replace()
use == its used for validations 

'''

# var1 = "123"
# var2 = "123sreeja"
#
# print(var1.isdigit())
# print(var2.isdigit())

phone_no1 = "1234567890"
phone_no2 = "1234567890 "  # the space is considered as string and hence validation failed

# print(phone_no1.isdigit())
# print(phone_no2.isdigit())

phone_no2 = phone_no2.strip()   # assign the updated value to new variable.
print(len(phone_no2))
print(phone_no2.isdigit())

var3 = ",,..Hello_there.my@namei$,,//||"
var33 = var3.strip()
print(var33)

var4 = ",, ..Hello_there.my@namei$,,//|| "
var44 = var4.strip()
print(var44)

var5 = var4.strip(",. ")
print(var5)

var6 = var4.strip("//||")  # need to check how to remove the backslash and pipe.
print(var6)

senn1 = "teh cat and teh dog"
senn1 = senn1.replace("teh","the")
print(senn1)            #the cat and the dog


sen2 = "https://www.google.com"
is_secure_url = sen2.startswith("https://")          # this gives boolean result
print(is_secure_url)

email_id = "sureshdasarwar@gmail.com"
is_valid_email = email_id.endswith("@gmail.com")
print(is_valid_email)

name = "suresh"
print(name.upper())

name = "RAVI"
print(name.lower())

