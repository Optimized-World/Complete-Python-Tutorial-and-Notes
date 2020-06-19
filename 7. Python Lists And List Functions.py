#################################### List and its Functions ###########################################

# Most versatile Data Type of Python is the list, 
# which can be written as a list of comma-separated values (items) between square brackets. 
# Lists might contain items of different types, but usually the items all have the same type.

# Ex:   
grocery = ["Harpic", "vim bar", "deodrant", "Bhindi",
           "Lollypop", 56, 4.56]

# The above list contains strings, integer and even float type data. 
# It means above list contains any kind of data means it’s not mandatory to form list of only one data type. 
# List can contain any kind of data in it.

# List elements are also accessed by using Indexes 
# i.e. first element of list possess 0 index then second as 1 and so on.

# Note : if you put any index which isn’t in the list 
# i.e. that index is not there in list then you will get an error.

print(grocery[5])  # Output : 56

# List Methods :

numbers = [2, 7, 9, 11, 3]
numbers.remove(9) # remove 9 from list
print(numbers)  # Output : [2, 7, 11, 3]

numbers = [2, 7, 9, 11, 3]
numbers.pop() # remove last element
print(numbers)  # Output : [2, 7, 9, 11]

numbers = [2, 7, 9, 11, 3]
# numbers.pop(2) # This will delete and return index 9 value
print(numbers.pop(2)) # return index # Output: 9
print(numbers)  # Output : [2, 7, 11, 3]

numbers = [2, 7, 9, 11, 3]
numbers.sort() # will sort the list
print(numbers)  # Output : [2, 3, 7, 9, 11]

numbers = [2, 7, 9, 11, 3]
numbers.reverse() # will reverse the list
print(numbers)  # Output : [3, 11, 9, 7, 2]

numbers = [2, 7, 9, 11, 3]
numbers.append(1) # will add 7 in the last of list
print(numbers)  # Output : [2, 7, 9, 11, 3, 1]

numbers = [] # Blank List
numbers.append(1) # will add 1 in the last of list
numbers.append(5) # will add 5 in the last of list
print(numbers)  # Output : [1, 5]

numbers = [2, 7, 9, 11, 3]
numbers.insert(2, 67) # will add 67 at index 2 in list
print(numbers)  # Output : [2, 7, 67, 9, 11, 3]

# List Slicing :

# List slices, like string slices are the sub part of a list extracted out. 
# You can use indexes of list elements to create list slices as per following format :

# Seq=list[start:stop:step]

numbers = [2, 7, 9, 11, 3]
print(numbers[0:5]) # Output : [2, 7, 9, 11, 3]
print(numbers[:5]) # Output : [2, 7, 9, 11, 3]
print(numbers[:]) # Output : [2, 7, 9, 11, 3]
print(numbers[1:]) # Output : [7, 9, 11, 3]
print(numbers[1:4]) # Output : [7, 9, 11]
print(numbers) # Output : [2, 7, 9, 11, 3]

# Extended Slice
# Default: 1st Parameter is 0, 2nd Parameter is Length of list, 3rd Parameter is 1

print(numbers[::]) # Output : [2, 7, 9, 11, 3]
print(numbers[::1]) # Output : [2, 7, 9, 11, 3]
print(numbers[::3]) # Output : [2, 11]

# Negative Step works only if first two parameters are blank
print(numbers[::-2]) # Output : [3, 9, 2]
print(numbers[0:3:-2]) # Output : [] / blank list
# So don't take any negative value as third parameter except -1

print(len(numbers)) # print length of list
# Output : 5
print(max(numbers)) # Output : 11
print(min(numbers)) # Output : 2

print(numbers) # Output : [2, 7, 9, 11, 3]
numbers[1] = 98
print(numbers) # Output : [2, 98, 9, 11, 3]

######### Tuple ##############

# Mutable - can change
# Immutable - cannot change

tp = (1, 2, 3)
print(tp) # Output: (1, 2, 3)
# tp[1] = 8 #=> Error : because tuple values can't be changed 

# Tuple with single Value
# tp = (1) # it act as variable so for tuple ',' required 
tp = (1,)
print(tp) # Output : (1,)

# Swap in Python
a = 1
b = 8
# Generally we do this 
# temp = a
# a = b
# b = temp

# In Python very simple
print(a, b) # Output : 1 8
a,b = b,a
print(a, b) # Output : 8 1

