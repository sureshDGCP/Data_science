print("Hello Suresh")

''' print(5+"2")
print("test")
'''

##print("5"+2)      # TypeError: can only concatenate str (not "int") to str

print("5+2")        # output is :5+2
print("5"+"2")      # output is : 52
c= 7
print("The result is "+ str(7))     #   The result is 7
# same datatypes can be concatenated

'''==================== variables ======= '''
## valid variable examples
name = "suresh"
NAME = "SREEJA"
Name = "SHRI ram"
_name = "_dummy_name"
name123 = 123

print(str(name123)+NAME,name,Name,_name)        #123SREEJA suresh SHRI ram _dummy_name

## invalid variables

##name@ = "test1"
#123name = "test2"
##t1 t2 = "test3"

##try = "test4"       #SyntaxError: invalid syntax
##print(try)

var1 = 5+2  ##(+ is operator and 5,2 is operand)

'''=============Data types ============='''

var2 = "cricket"

print(type(var2)) ## type is keyword to check the datatype of variable   (<class 'str'>)

var3 = -3
var4 = 55
print(type(var3),type(var4))   ##<class 'int'> <class 'int'>

var5 = 23.56
print(type(var5))   ## <class 'float'>

var6 = True
var7 = False
print(type(var6),type(var7))   ## <class 'bool'> <class 'bool'>