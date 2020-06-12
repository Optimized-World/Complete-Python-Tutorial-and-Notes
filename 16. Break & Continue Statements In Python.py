# i = 0

# while(i<45):
#     print(i+1)
#     i = i+1

i = 0

while(True):
    print(i+1, end =" ")
    if(i==44):
        break # Stop the loop
    i = i+1
# after break comes here

# continue used to not execute codes below it in loop

# if we want to print numbers which are greater than 5
while(True):
    if i+1<5:
        i = i+1
        continue
    print(i+1, end =" ")
    if(i==44):
        i = i+1
        break # Stop the loop
    i = i+1

# Quiz
# Keep taking input till user enter number grater than 100

while(True): 
    num = input("Please enter a number") 
    if( int(num)<100): 
        continue 
    else: 
        print("congratulations, you entered number >= 100") 
        break


