
var1 = 12 # "=" is the assignment operator

age = 23
print(age)   ## Space in python has special meaning, which considers it as indentation, similarly for tab

##============================== Expressions =====================

a = 2+3     ## this is an expression and its combination of operators and operands

x = 5*2+3*4
print(x)   ## order of operation follows BODMAS rule
# B= () brackets, o = square root, D = division(/), M = Multiplication, A = Addition, S = Subtraction

print(10/(2+3))  ## 2.0 is output
print(10/2+3)    ## 8.0 is output

print(5/2.5) # 2.0 is output
print(6/2)   # 3.0 is output

print(15/3*2+3-8/2)

##==================== String concatenation ==============

a = "Hello"
b = "World"
print(a+" "+b)

#==================== Exercises ================

name = input("Please tell me your name:")
print(f"Hi {name} welcome to college")

#a = "*"+10  #TypeError: can only concatenate str (not "int") to str
print(a)

b = "*"*10
print(b)    #output is **********

#==================== Length of string =============================================

username = "Sreeja"
print(len(username))

#====================== Accessing characters in string =============================

name = "Ravi"  # index starts from  0 1 2 3 in python
print(len(name))  # output is 4

print(name[0])  # it will give "R"
print(name[1])  # it will give "a"
print(name[2])  # it will give "v"
print(name[3])  # it will give "i"

name1 = "Hello there lets learn Python"
print(name1[23:29])    #slicing of strings 23 is start of index for word python and 29 is end of index since its exclusive so we need to consider one extra index.

print(name1[21:])   # this will print "n Python" as output since it consider the rest of indices if we don't mention explicit

print(name1[:8])    # this will print "Hello th" as output since it has considered index from 0

print(name1[:])     # this will be print "Hello there lets learn Python"