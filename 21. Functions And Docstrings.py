############ Functions and Docstrings Tutorial #################

# Function helps in code reuseability

##########################################

## Example of built in function

a = 9
b = 8
# Sum is a inbuilt function in Python 
# takes tuple or list (more, general Iterables) as input
c = sum((a,b)) 
print(c) # Output : 17

##########################################

## Example of user defined function

## The keyword def introduces a function definition. 
# It must be followed by the function name and 
# the parenthesized list of formal parameters. 
# The statements that form the body of the function 
# start at the next line, and must be indented.

def function1():
    print("Hello you are in function 1")

function1() # Output : Hello you are in function 1

##### Functions with Parameter & Return Statement ####

# The 'return' statement returns with a value from a function.
# 'return' without an expression argument returns None
# if no 'return' statement used in function , 
# then function returns None
 
print(function1()) 
# Output : Hello you are in function 1 (due to function call)
#        : None (due to no return statement)

## Functions with parameters

def function2(a,b):
    print("You are in function 2,","Sum :",a+b)

function2(5,7) 
# Output :You are in function 2, Sum : 12



def function3(a,b):
    average = (a+b)/2
    print("Average :",average)

function3(5,7) 
# Output : Average : 6.0



# If we want to store value calculated by function in a variable
# We have to use return statement
def function4(a,b):
    average = (a+b)/2
    # print("Average :",average)
    return average
val = function4(5,7) 
print(val)
# Output : 6.0


################ Doc strings ##################

# Used to store information about function
# """ Documentation """ or ''' Documentation '''
# # This is not a comment but docstring ...
# ...if written as first line in function
# written elsewhere in function treated as comment
def function5(a,b):
    '''This is a function which calculates average of two numbers'''
    average = (a+b)/2
    return average

print(function5.__doc__)
# Output : This is a function which calculates average of two numbers

# docstring is helpful to know about functions 
# in diiferent imported modules 
# Also if we have large no. of functions 
# we can use docstring to know about function 
 

