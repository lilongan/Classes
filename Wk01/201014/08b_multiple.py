name = input("What is your name?")
num = len(name)
## You can have multiple conditions here
if num > 3 and num < 15: # Both statements must be truthy
    if num == 4:
        print('Perfect length!')
    else:
        print("It's an okay length.")
    print(f"Welcome {name}.")
else:
    print('%s is not a good number of characters' % len(name))

if num > 3 or num < 15: # either statement must be truthy
    print("This is valid") # If input 2 because less than 15; 26 is greater than 3

#if num < 3 or num > 15:
    print("Your number is not between 3 and 15")
#else:
    print('Normal lengthed name.')

name = input("Give me your name.")
if not name:
    print("You must give a name.")
else:
    print(name)
    