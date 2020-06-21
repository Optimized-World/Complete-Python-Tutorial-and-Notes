############### Short Hand If Else Notation Tutorial ###############

a = int(input("enter a :\n"))
b = int(input("enter b :\n"))

# Concise but not Obivious Readability in Code
if a>b: print("A is greater than B")

# Less Concise but Better Readability in Code
if a>b: 
    print("A is greater than B")

# This is a Trade-off, use which suit best for you team.

# Short if else
print("A is greater than B") if a>b else print("A is less than or equal to B")



