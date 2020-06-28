##################### Writing Appending to a File ##################

# f is better to say file handle which open() return
# instead saying it pointer but commonly f also known as file pointer

# Opening file in write,text mode
# Only 'w' mentioned below because t-text mode is by default
# So 'w' is same as 'wt'

# IF file "26. Tutorial.txt" not exist then it will create that.
# If alrady exist then it will replace all the content with what we will write in the file
f = open("26. Tutorial1.txt", "w")
f.write("Rural Development Party - A party that contests only gram panchayat elections and has the vision to make World Class Villages with limited resources.\n")
f.close()

# If we again do f.write on same file it just replace content
# but in most cases we want to append the content in the file at end
# for that open file in append mode -'a'
f = open("26. Tutorial1.txt", "a")
# due to newline character "\n" at the last of previous write
# this content will appended in new line.
f.write("Rural Development Party - A party that contests only gram panchayat elections and has the vision to make World Class Villages with limited resources.\n")
f.close()

## To get no. of characters written
f = open("26. Tutorial2.txt", "w")
# f.write returns no. of characters written
a = f.write("Rural Development Party - A party that contests only gram panchayat elections and has the vision to make World Class Villages with limited resources.\n")
print(a) 
# Output : 150
f.close()

f = open("26. Tutorial2.txt", "a")
# f.write returns no. of characters written
a = f.write("Rural Development Party - A party that contests only gram panchayat elections and has the vision to make World Class Villages with limited resources.\n")
print(a) 
# Output : 150
f.close()


# Handle read and write both in a file 
# Open file in both read and write mode "r+"

## NOTE : "r+" mode don't create file automatically 
# as in write and append mode
# because here we can do read first 
# which will not run if file don't exist already so careful
f = open("26. Tutorial3.txt", "r+")
f.write("Thank You")
content = f.read()
# you don't get anything printed 
# because file pointer move to the last position after writing
print(content)
f.close()

f = open("26. Tutorial3.txt", "r+")
# it will print "Thank You" as file pointer is at starting
content = f.read()
print(content)
f.write("Thank You")
f.close()