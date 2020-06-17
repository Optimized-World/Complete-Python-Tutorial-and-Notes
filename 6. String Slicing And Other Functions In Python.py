################### Strings : #####################
mystr = "Vivek is a good boy"
print(len(mystr))
# Output: 19

### Note : The indexes of a string begin from 0 to (length-1) in forward direction 
# and -1,-2,-3,…,length in backward direction.

print(mystr[4])
# 5 is excluded but 0 included
print(mystr[0:5])

# Output: k
# Output: Vivek

### Error :
# print(mystr[78])

# gives full string here no error
print(mystr[0:78])

# Output :

#Print with skip characters 
print(mystr[::2])
# Every second character will be printed starting from 0

#Print with skip characters in limmited range
print(mystr[0:5:2])

#print string in reverse order
print(mystr[::-1])

#Print with skip characters in reverse order
print(mystr[::-2])

## Some String Functions

print(mystr.endswith("bdoy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.replace("is", "are"))


############################ Extra Content ##################################

# If you don’t want characters prefaced by \ to be interpreted as special characters, 
# you can use raw strings by adding an r before the first quote:

# >>> print('C:\some\name')  # here \n means newline!
# C:\some
# ame
# >>> print(r'C:\some\name')  # note the r before the quote
# C:\some\name



# String literals can span multiple lines. 
# One way is using triple-quotes: """...""" or '''...'''. 
# End of lines are automatically included in the string, 
# but it’s possible to prevent this by adding a \ at the end of the line. 
# The following example:

# print("""\
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# """)

# produces the following output (note that the initial newline is not included):

# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to



# Strings can be concatenated (glued together) with the + operator, and repeated with *:

# >>>
# >>> # 3 times 'un', followed by 'ium'
# >>> 3 * 'un' + 'ium'
# 'unununium'

# Two or more string literals (i.e. the ones enclosed between quotes) 
# next to each other are automatically concatenated.

# >>>
# >>> 'Py' 'thon'
# 'Python'

# This feature is particularly useful when you want to break long strings:

# >>> text = ('Put several strings within parentheses '
# ...         'to have them joined together.')
# >>> text
# 'Put several strings within parentheses to have them joined together.'


# This only works with two literals though, not with variables or expressions:

# >>>
# >>> prefix = 'Py'
# >>> prefix 'thon'  # can't concatenate a variable and a string literal
#   File "<stdin>", line 1
#     prefix 'thon'
#                 ^
# SyntaxError: invalid syntax
# >>> ('un' * 3) 'ium'
#   File "<stdin>", line 1
#     ('un' * 3) 'ium'
#                    ^
# SyntaxError: invalid syntax


# If you want to concatenate variables or a variable and a literal, use +:

# >>>
# >>> prefix + 'thon'
# 'Python'
