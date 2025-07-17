age = 10
print(age)

# print(name)
# name = suresh  ## declaration should be first and use should be later

age2 = 23
print(age,age2)
print("Lecturere's age is:"+str(age)+"Principal's age is:"+str(age2) )

print("Lecturere's age is: {} and Principal's age is: {}".format(age,age2))  ## place holder example for printing
var1 = "Suresh"
var2 = True
var3 = 100
var4 = 10.5
print("This is var1 {} and var2 {} and var3 {} and var4 {} ".format(var1,var2,var3,var4))
print("This is var1 {} and var2 {} and var3 {} and var4 {} ".format(var4,var2,var3,var1))  ## these are positional arguments

print("My age is {} ".format(age)) ## self in format() is the statement we pass in with placeholder in print statement e.g. "My age is {}"

print("myname is {name}".format(name="Sreeja"))  ## this an example of kwargs and it takes the keywards inside the positional agrs e.g. {name} and defined in format section.

print("myname is {name}, and I live in {place}".format(place="HYD", name="Sreeja"))  ## this an example of kwargs which shows position doesnt matter since we passed the keywarda as agruments

##print("myname is {name}, and I live in {place} and my fav foodtype is {food}".format(place="HYD", name="Sreeja")) ## its expects the keyward agrs inf format

##=========================== F strings  ========================

print("My name is {}".format(var1))   ## it makes the format syntax more simpler
print(f"My name is {var1}")         #My name is Suresh
print("my name is {exx2}".format(exx2="123"))       #my name is 123
