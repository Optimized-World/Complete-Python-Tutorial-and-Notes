#############  Variable -: ################

# A variable is a name which is given to any storage area 
# or memory location in a program.
# Actually, Variable doesn’t hold a value 
# but it’s the name given to any memory address in RAM. 
# It means variable is the way to access that memory address of Ram
# so that we can store and manipulate data in that memory address or memory block.

# It’s a name of memory location.

# In simple words we can say that variable is a container
# which contains some kind of information 
# and whenever we need that information 
# then we simply use that container or open it.

###### Rules for defining a variable in Python : ######

## Variable name can contain alphabets, digits, and underscore (_).
# For E.g. : demo_xyz = ‘It’s a string variable’

##Variable name can start with an alphabet and underscore only.
# For E.g. : _demo, de_mo, etc.

### It can’t start with a digit.
### No white-space and reserved keywords are allowed to use as a variable name.

# Python is an intelligent language 
# i.e. it automatically defines the type of data. 
# It means we just need to put some data in a variable 
# then Python automatically understands what kind of data variable is holding.


# String Variables

var1 = "hello world"
print(var1)
var1 = "54"
var4 = "32"

# Integer(int) Variable

var2 = 4

# Float Variable

var3 = 36.7

######### Typecasting : ############

## It is the way to change the data type of one data to another 
## i.e. it changes the data type of any variable or data to any other data type.

## I know it’s bit confusing but let me tell you in a simply manner. 
## Suppose there is a string “34” and 
# as we know we can’t add this to any integer number let’s say 6. 
# But to do so we can typecast string to int data type 
# and then we can add 34+6 and we will get the output as 40.

#### There are many functions to convert one data type into another type :

"""
str()
int()
float()
"""
## str() – this function allows us to convert data type into string.
## int() – this function allows us to convert data type into integer.
## float() – this function allows us to convert data type into floating point number 
# i.e. no. with decimals.

print(str(int(var1) + int(var4)) )
print("Hello world\n")

# to print some thing multiple times

print(100 * str(int(var1) + int(var4)) )
print(100 * "Hello world\n")

#### input() Function – 
# This function allow user to input something in the program as a string.
# input() function always takes input as a string 
# i.e. if we ask user to input a number then also it will take it as a string 
# and then we have to typecast it into either int or float data type. 

print("Enter your number")
inpnum = input()
print("You entered", int(inpnum)+10)



"""
Quiz - Solved in the Tutorial
Exercise - Next Tutorial
Project - Some awesome python utility
"""

# Quiz : Create a program which takes two number input from user 
# and then give output as a sum of these numbers.



# Solution
# Addition Program
print("Enter first number")
n1 = input()
print("Enter second number")
n2 = input()
print("Sum of these two numbers is", int(n1) + int(n2))