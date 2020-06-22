#### Exercise 2 - Faulty Calculator ###
## Problem Statement
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

# Solution : 

# Input Part
Calculator_On = True
print('Welcome, You Calculator is ready to serve you !')
while(Calculator_On==True):
    x = int(input('Please enter First number : '))
    y = int(input('Please enter Second number : '))
    operator = input('Please Select Operator from these {*,/,+,-} : ')

    # Output Part
    if(operator == '*'):
        if(x == 45 and y == 3):
            print('Output : ',555)
        else:
            print('Output : ',x*y)
    elif(operator == '/'):
        if(x == 56 and y == 6):
            print('Output : ',4)
        else:
            print('Output : ',x/y)
    elif(operator == '+'):
        if(x == 56 and y == 9):
            print('Output : ',77)
        else:
            print('Output : ',x+y)
    elif(operator == '-'):
        print('Output : ',x-y)
    
    print(' Do you want to calculate again?','\n','Please type 1 for YES or 0 for NO.')
    Calculator_On = int(input())
    if(Calculator_On == False):
        print('Thank you, Hope you will use me again !')
