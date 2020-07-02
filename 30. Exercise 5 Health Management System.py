########## Exercise 5: Health Management System ##########

# Health Management System
# Lets our company designs diet and exercises 
# for our clients.
# Let we have 3 clients - Vivek, Anita and Ganesh

# You have to make 3 Files 
# to lock(means store) foods of clients.
# and 3 files to lock their exercises
# Total 6 files

# NOTE : We are not implementing user registration
# in this program so you have to manually create
# 6 text files for three clients.
# File names are following : 
# Client1_diet.txt,Client2_diet.txt,Client3_diet.txt
# Client1_exercises.txt,Client2_exercises.txt,Client3_exercises.txt

# Program Structure:

# First take input 
# 1 for ADMIN LOGIN 
# 2 FOR USER LOGIN

# For ADMIN LOGIN take only password
# and for USER LOGIN take both id and password.

# For USER LOGIN :
# Use following credentials:
# IDs : 1 for "Vivek", 2 for "Anita", 3 for "Ganesh
# PASSWORDs : 
# "Vivek@123" for "Vivek",
# "Anita@123" for "Anita", 
# "Ganesh@123" for "Ganesh"

# If Password and Id matches for user
# Print : You are Logged In.
# Else Print : Authentication fails, Please try again

# write a function to ask the client 
# what he wants to lock(store data) :
# 1 for Food/diet or 2 for Exercise

# use below function to get time:
def getdate():
    import datetime
    return datetime.datetime.now()

# Writing format in file:
# Heading format
# TIME STAMP    |      FOOD/DIET

# Content format
# [time]  [roti, rice, paneer masala] 

# Similar Format for exercise file

# For ADMIN LOGIN :
# Ask password to admin 
# Admin password : "admin@123"
# If Password matches
# Print : You are Logged In as Admin.
# Else Print : Authentication fails, Please try again

# once admin verified ask client Id to admin
# and then what he wants to retrieve :
# 1 for Food/diet or 2 for Exercise
# One more function for admin 
# to retrieve exercise or food for any clients 
# provide data of that client

# Solution :

# You code here


  
