# A set is an unordered collection 
# with no duplicate elements. 
# Basic uses include membership testing 
# and eliminating duplicate entries. 
# Set objects also support mathematical operations 
# like union, intersection, difference, 
# and symmetric difference.

s = set()
print(type(s)) # Output :  <class 'set'>

l = [1, 2, 3, 4]
s_from_list = set(l)
print(s_from_list)
# Output :  {1, 2, 3, 4}
print(type(s_from_list))
# Output :  <class 'set'>

s.add(1) # 1 will be added to empty set s
print(s) # Output :  {1}

s.add(1) # Nothing change  as set stores unique items
print(s) # Output :  {1}

s.add(2)
print(s) # Output :  {1, 2}

s.remove(2) # Remove 2 from set 
print(s) # Output :  {1}

# Union of set s and {1, 2, 3}
s1 = s.union({1, 2, 3})
print(s, s1) # Output : {1} {1, 2, 3}

# Intersection of set s and {1, 2, 3}
s1 = s.intersection({1, 2, 3})
print(s, s1) # Output : {1} {1}

s = {1, 4, 5, 6, 6}
print(len(s)) # Output : 4
print(max(s)) # Output : 6
print(min(s)) # Output : 1

s = {1, 2}
s1 = {4, 6}    
print(s.isdisjoint(s1)) # Output : True 

############# Extra Content #######################

# >>> # Demonstrate set operations on unique letters from two words
# ...
# >>> a = set('abracadabra')
# >>> b = set('alacazam')
# >>> a                                  # unique letters in a
# {'a', 'r', 'b', 'c', 'd'}
# >>> a - b                              # letters in a but not in b
# {'r', 'd', 'b'}
# >>> a | b                              # letters in a or b or both
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
# >>> a & b                              # letters in both a and b
# {'a', 'c'}
# >>> a ^ b                              # letters in a or b but not both
# {'r', 'd', 'b', 'm', 'z', 'l'}

# set comprehensions are also supported:

# >>>
# >>> a = {x for x in 'abracadabra' if x not in 'abc'}
# >>> a
# {'r', 'd'}
