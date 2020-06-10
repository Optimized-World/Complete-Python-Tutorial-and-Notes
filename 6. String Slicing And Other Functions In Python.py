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


print(mystr.endswith("bdoy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.replace("is", "are"))
