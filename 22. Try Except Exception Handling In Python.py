################# Try Except Exception Handling Tutorial ##############

# Lets assume we running something in our python program
# which may or may not throw error

# For, Example :

"""
print("Enter num 1 :")
num1 = int(input()) # Expect a number as input
print("Enter num 2 :")
num2 = int(input()) # Expect a number as input
print("Sum of these two numbers is",num1+num2)
"""

# Above program will give error if input is not a number

# Input :

# $ python 22.\ Try\ Except\ Exception\ Handling\ In\ Python.py 
# Enter num 1 :
# re

# Output : error in line 2
# ValueError: invalid literal for int() with base 10: 're'

"""
print("Enter num 1 :")
num1 = input() # Expect a number as input
print("Enter num 2 :")
num2 = input() # Expect a number as input
print("Sum of these two numbers is",int(num1)+int(num2))

# It will not get printed due to error in line 5
print("This line is very important") 
"""

# Above program will give same error at line 5 of program(actually line 29)
# if input is not a number


# But if we have some thing very important
# to run after this error occuring line.
# Due to error, program stops there 
# and important part will not executed

# So to handle errors and proceed/run the program below
# the error we use try exception
# Lets see the example :


print("Enter num 1 :")
num1 = input() 
print("Enter num 2 :")
num2 = input() 
try: # try it else run exception and proceed
    print("Sum of these two numbers is",
            int(num1)+int(num2))
except Exception as e:
    print(e)

print("This line is very important")

## Input :
# Enter num 1 :
# wee
# Enter num 2 :
# 5

## Output :
# invalid literal for int() with base 10: 'wee'
# This line is very important

## Input :
# Enter num 1 :
# 8
# Enter num 2 :
# 7

## Output :
# Sum of these two numbers is 15
# This line is very important


# Try and Exception is useful in many places
# For Example : 
# when we work with internet connectivity
# lets assume program have to download something 
# and internet speed is slow
# In these condition, we don't want to stops program
# instead provides a error message about poor internet connection
# and proceed the program 











