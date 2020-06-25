# Take a number n in program
# Ask user to guess the number 
# tell user whether number entered is 
# greater,less or user guessed the number correctly
# no . of guesses allowed to user is 9
# keep printing no of guesses left
# if user can guess number in allowed chances 
# Print Game over You win 
# Print No. of gusess you took to finish
# else Game over You lose

##### Solution ######

n = 453
guesses_left = 9
print("Starting the Game \"*GUESS NUMBER*\" ....... ")
print("Guesses Left : ",guesses_left)
print("Enter your guess : ", end =' ')
num = int(input())
while(True):
    if num==n:
        guesses_left-=1
        print("Great, You guessed the number.\nYou took ",9-guesses_left," guesses to finish !!")
        print("Congratulation, You win !!")
        break
    elif num>n:
        guesses_left-=1
        print("You entered a greater number.")
        if guesses_left == 0:
            print("Ohh, You lose. Game Over :)")
            break
        print("Guesses Left : ",guesses_left)
        print("Please try again. Enter your guess : ", end =' ')
        num = int(input())
        continue
    else:
        guesses_left-=1
        print("You entered a smaller number.")
        if guesses_left == 0:
            print("Ohh, You lose. Game Over :)")
            break
        print("Guesses Left : ",guesses_left)
        print("Please try again. Enter your guess : ", end =' ')
        num = int(input())
        continue





