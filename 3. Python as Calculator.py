#### Python as a Calculator :

## First of all I would like to tell one thing 
# i.e. the main motive of using Python is not to do calculations, 
# yeah that’s true Python is not just limited to do calculations. 
# It has vast no. of uses and has many merits or advantages. 
# Using Python you can do anything, literally saying anything 
# such as creating games, apps, software’s, websites, etc. 

# To do calculation in Python, 
# open Windows PowerShell and in that type python to open Python interpreter. 

# >>> 4 + 8
# 12
# >>> 5*7
# 35

#  Then simply type or put whatever mathematical calculation you want to do.


##################################### Extra Content ##########################################

#### More Examples ####

# >>> (50 - 5*6) / 4
# 5.0
# >>> 8 / 5  # division always returns a floating point number
# 1.6

## NOTES

## Division (/) always returns a float. 
# To do floor division and get an integer result (discarding any fractional result)
#  you can use the // operator; 
# to calculate the remainder you can use %:

# Example :

# >>> 17 / 3  # classic division returns a float upto 15 precision point
# 5.666666666666667
# >>>
# >>> 17 // 3  # floor division discards the fractional part
# 5
# >>> 17 % 3  # the % operator returns the remainder of the division
# 2
# >>> 5 * 3 + 2  # result * divisor + remainder
# 17

# With Python, it is possible to use the ** operator to calculate powers:
# Since ** has higher precedence than -, 
# -3**2 will be interpreted as -(3**2) and 
# thus result in -9. To avoid this and get 9, you can use (-3)**2

# >>>
# >>> 5 ** 2  # 5 squared
# 25
# >>> 2 ** 7  # 2 to the power of 7
# 128

## The equal sign (=) is used to assign a value to a variable. 
# Afterwards, no result is displayed before the next interactive prompt:

# >>> width = 20
# >>> height = 5 * 9
# >>> width * height
# 900


## If a variable is not “defined” (assigned a value), trying to use it will give you an error:

# >>> n  # try to access an undefined variable
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'n' is not defined


## There is full support for floating point; 
# operators with mixed type operands convert the integer operand to floating point:

# >>> 4 * 3.75 - 1
# 14.0

## In interactive mode, the last printed expression is assigned to the variable _. 
# This means that when you are using Python as a desk calculator, 
# it is somewhat easier to continue calculations, for example:

# >>> tax = 12.5 / 100
# >>> price = 100.50
# >>> price * tax
# 12.5625
# >>> price + _
# 113.0625
# >>> round(_, 2)
# 113.06

##  Python also has built-in support for complex numbers, 
# and uses the j or J suffix to indicate the imaginary part (e.g. 3+5j).





