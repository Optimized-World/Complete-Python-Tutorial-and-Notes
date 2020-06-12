# Create a dictionary and take input from the user and return the meaning of the
# word from the dictionary

Dict = {"ignore":"refuse to take notice of or acknowledge", "abandon":"cease to support or look after",
        "exaggerate":"enlarged or altered beyond normal proportions", "prejudice":"preconceived opinion that is not based on reason or actual experience"}
print("Enter the Word")
Data1 = input()
print(Data1, "means", Dict[Data1])
