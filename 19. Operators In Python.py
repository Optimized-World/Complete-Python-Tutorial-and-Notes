############# Operators in Python #############

#### Operators :

# Arithmetic Operator 
# Assignment Operator
# Comparison Operator
# Logical Operator 
# Identity Operator
# Membership Operator
# Bitwise Operator

# Arithmetic Operator : helps in numerical claculations
print("Arithmetic Operators :")

print("5 + 6 is",5+6) 
# Output : 5 + 6 is 11
print("5 - 6 is",5-6) 
# Output : 5 - 6 is -1
print("5 * 6 is",5*6) 
# Output : 5 * 6 is 30
print("5 / 6 is",5/6) 
# Output : 5 / 6 is 0.8333333333333334

# // Gives floor division
print("5 // 6 is",5//6) # It divide and give only Integer part
# Output : 5 // 6 is 0 
print("15 // 6 is",15//6) 
# Output : 15 // 6 is 2

# Power operator
print("5 ** 3 is",5**3) 
# Output : 5 ** 3 is 125

# Modulous/Remainder Operator
print("5 % 3 is",5%3) 
# Output : 5 % 3 is 2

#### Assignment Operator : to assign values
print("Assignment Operators :")
x = 5
print(x) # Output : 5
x += 7 # x = x + 7
print(x) # Output : 12

x = 5
print(x) # Output : 5
x -= 7 # x = x - 7
print(x) # Output : -2

x = 5
print(x) # Output : 5
x *= 7 # x = x * 7
print(x) # Output : 35

x = 5
print(x) # Output : 5
x /= 7 # x = x / 7
print(x) # Output : 0.7142857142857143

# Other Operators : '%=' ,'**=', etc. Try Out 

### Comparison Operators
print("Comparison Operators :")

i = 5
print(i == 5) # Output : True
i = 8
print(i == 5) # Output : False
print(i != 5) # Output : True
print(i > 5) # Output : True
print(i < 5) # Output : False
print(i >= 5) # Output : True
print(i <= 5) # Output : False

#### Logical Operators :
print("Logical Operators :")

# and, or ,not
a = True
b = False
print(a and a) # Output : True
print(a and b) # Output : False
print(a or b) # Output : True
# not give opposite bool value
print(not b) # Output : True

#### Identity Operators :
print("Identity Operators :")

print(a is not b) # Output : True
print(5 is not 5) # Output : False
print(5 is 5) # Output : True

#### Membership Operators :
print("Membership Operators :")

list = [3,3,2,2,39,33,35,32]
print(32 in list) # Output : True
print(324 in list) # Output : False
print(324 not in list) # Output : True

##### Bitwise Operator :
print("Bitwise Operators :")

# Binary
# 0 - 00 
# 1 - 01
# 2 - 10
# 3 - 11

# AND bitwise operator
print(0 & 1) # Output : 0
# OR bitwise operator
print(0 | 1) # Output : 1

##### Some Bitwise Operators and Description :

#################################################################################
#   Operator    #                  Description                                  #                                           #
#################################################################################
#      & AND    # Sets each bit to 1 if both bits are 1                         # 
#################################################################################
#      | OR     # Sets each bit to 1 if one of two bits is 1                    #
#################################################################################
#      ^ XOR    # Inserts a double character in the text a that point.          #
#################################################################################
#      ~ NOT    # Inserts a single quote character in the text at that point.   #
#################################################################################
#  << Zero fill #        Shift left by pushing zeros in from the right,         #
#   left shift  #            and let the leftmost bits fall off                 #
#################################################################################
#   >> Signed   #      Shift right by pushing copies of the leftmost bit        #
#  right shift  #      from the left and let the rightmost bits fall off.       #
#################################################################################









