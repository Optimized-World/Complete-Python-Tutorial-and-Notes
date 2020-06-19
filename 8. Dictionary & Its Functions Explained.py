# Dictionary is nothing but key value pairs
d1 = {}

print(type(d1)) # Output : <class 'dict'> 
# List : [], tuple : (), dict : {}

d2 = {"Vivek":"Burger",
      "Rohan":"Fish",
      "SkillF":"Roti"}
print(d2)
# Output : {'Vivek': 'Burger', 'Rohan': 'Fish', 'SkillF': 'Roti'}

print(d2['Vivek']) # Output : Burger

####### About Key ###########

# you can use an integer, float, string, tuple or Boolean 
# as a dictionary key. 
# However, neither a list nor another dictionary 
# can serve as a dictionary key,
# because lists and dictionaries are mutable.

############ About Values ############

# Any thing can be used as value

d2 = {"Vivek":"Burger",
      "Rohan":"Fish",
      "SkillF":"Roti",
      "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}

print(d2["Shubham"]["B"]) # Output : maggie

# Adding more key value pairs to dictionary
d2["Ankit"] = "Junk Food"
print(d2)
# Output : {'Vivek': 'Burger', 'Rohan': 'Fish', 'SkillF': 'Roti', 'Shubham': {'B': 'maggie',
#  'L': 'roti', 'D': 'Chicken'}, 'Ankit': 'Junk Food'}

# Changing value in dictionary
d2["Ankit"] = "Fresh Food"
print(d2)
# Output : {'Vivek': 'Burger', 'Rohan': 'Fish', 'SkillF': 'Roti', 'Shubham': {'B': 'maggie',
#  'L': 'roti', 'D': 'Chicken'}, 'Ankit': 'Fresh Food'}

d2[420] = "Kebabs"
print(d2)
# Output : {'Vivek': 'Burger', 'Rohan': 'Fish', 'SkillF': 'Roti', 'Shubham': {'B': 'maggie',
# 'L': 'roti', 'D': 'Chicken'}, 'Ankit': 'Fresh Food', 420: 'Kebabs'}

del d2[420]
print(d2)
# Output : {'Vivek': 'Burger', 'Rohan': 'Fish', 'SkillF': 'Roti', 'Shubham': {'B': 'maggie',
#  'L': 'roti', 'D': 'Chicken'}, 'Ankit': 'Fresh Food'}

print(d2["Shubham"])
# Output : {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}

d3 = d2.copy()
del d3["Vivek"] # It will delete from d3 only not from d2
print(d2)
# Output : {'Vivek': 'Burger', 'Rohan': 'Fish', 'SkillF': 'Roti', 
# 'Shubham': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Ankit': 'Fresh Food'}
print(d3)
# Output : {'Rohan': 'Fish', 'SkillF': 'Roti', 
# 'Shubham': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Ankit': 'Fresh Food'}

# here d2 point to a dictionary and d3 also points to same dictionary
d3 = d2
del d3["Vivek"] # It will delete from both d2 and d3
print(d2)
# Output : {'Rohan': 'Fish', 'SkillF': 'Roti', 
# 'Shubham': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Ankit': 'Fresh Food'}
print(d3)
# Output : {'Rohan': 'Fish', 'SkillF': 'Roti', 
# 'Shubham': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Ankit': 'Fresh Food'}

# Adding more key value pairs to dictionary
d2.update({"Leena":"Toffee"})
print(d2)
# Output : {'Rohan': 'Fish', 'SkillF': 'Roti', 'Shubham': {'B': 'maggie', 
# 'L': 'roti', 'D': 'Chicken'}, 'Ankit': 'Fresh Food', 'Leena': 'Toffee'}

# print all keys of dictionary as list
print(d2.keys())
# Output : dict_keys(['Rohan', 'SkillF', 'Shubham', 'Ankit', 'Leena'])

# print all keys-value pair of dictionary as tuple in list
print(d2.items())
# Output : dict_items([('Rohan', 'Fish'), ('SkillF', 'Roti'), 
# ('Shubham', {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}), 
# ('Ankit', 'Fresh Food'), ('Leena', 'Toffee')])
