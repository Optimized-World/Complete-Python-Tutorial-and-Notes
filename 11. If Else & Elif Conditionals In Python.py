## If , elif and else

var1 = 6
var2 = 56
# take input in var 3 and typecast it to integer
var3 = int(input("Please enter an integer: "))
## Console ## Please enter an integer: 42

if var3>var2:
    print("Greater")
elif var3==var2:
    print("Equal")
else:
    print("Lesser")
# Output : Lesser

list1 = [5, 7, 3]
print(5 in list1) # Output : True
if 15 not in list1:
    print("No its not in the list")
# Output : No its not in the list


# Quiz
# Ques : Write program to check whether 
# you are above,equal to or less than 18.
# Give a sample allowed task to each age group

print("What is your age?")
age = int(input())
if age<18:
    print("You cannot drive")
elif age==18:
    print("We will think about you")
else:
    print("You can drive")



