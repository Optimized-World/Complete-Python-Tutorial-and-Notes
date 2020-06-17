################################################################################

########### Python Comments: #############

# =>> Comments are used to make the code more understandable for programmer.
# =>> Comments are not executed by Interpreter.

## There are 2 methods to write comment in Python Language -:
# => Single Line Comment
# => Multi Line Comment

# Single Line Comment : Single Line comments are the comments 
#                       which are created in single line only 
#                       i.e. they occupy the space of single line only.
# We use '#' (hash/pound to write single line comment).
# E.g. 
# this is a comment.

## Multi Line Comment : Multi Line comments are the comments 
#                       which are created by using multiple lines 
#                       i.e. they occupy more than one line in the program.

## We use """ ….. Comment …. """ for writing multi line comment 
# i.e. (tripe quotes for writing multi-line comments).

text = "# This is not a comment because it's inside quotes."

"""
This is a
Multiline Comment
"""

"""
This is a comment
"""

########################################################################################

# Print Function in Python

# print() is a function in Python language 
# which allows us to display whatever is written it 
# i.e. inside print statement.

print("This is a Demo")
print(5+4)
print("Hello","Worlds!!")

# Output
#> python '.\4. Comments, Escape Sequences & Print Statement.py'
# This is a Demo
# 9
# Hello Worlds!!

#########################################################################################

# end command:

# end command allows us to put something in the end of line 
# i.e. in simple words it allows us to continue the line with ‘ ’ or ‘,’
# or anything whatever we put inside these quotes of end. 
# It simply joins two different print statements using some kind of symbol or even by space.
# if we don't use/write any thing, by default '\n'=>new line used as end command

print("Hello",end=' ')
print("World !!")
print("Hey",end='!!')

# Output
#> python '.\4. Comments, Escape Sequences & Print Statement.py'
# Hello World !!
# Hey!!

######################################################################################

# Escape Sequences :

# An Escape Sequence in Python programming language is a sequence of characters.
# It doesn’t represent itself when used inside string literal or character.
# It is composed of two or more characters starting with backslash \.

# print("next line")
print('\n')
print("Subscribe CodeWithHarry now","Bhai video bhi like kar dena")
print("C:\narry")
print("C:\\narry")
print("Harry is \n good boy \t1")

#Output 

#> python '.\4. Comments, Escape Sequences & Print Statement.py'

# Subscribe CodeWithHarry now Bhai video bhi like kar dena
# C:
# arry
# C:\narry
# Harry is
#  good boy       1

########################## Commonly used Escape Sequences #######################

#################################################################################
#   Escape      #                  Description                                  #
#   Sequence    #                                                               #
#################################################################################
#      \n       # Inserts a newline in the text at that point.                  #
#      \\       # Inserts a back slash character in the text at that point.     #
#      \"       # Inserts a double character in the text a that point.          #
#      \'       # Inserts a single quote character in the text at that point.   #
#      \t       # Inserts a tab in the text at that point.                      #
#      \f       # Inserts a form feed in the text at that point.                #
#      \r       # Inserts a carriage return in the text at that point.          #
#      \b       # Inserts a backspace in the text at that point.                #
#################################################################################