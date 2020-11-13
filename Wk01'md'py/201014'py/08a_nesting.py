#nesting putting one thing inside another
name = input("What is your name?")

if len(name) > 3: #counting the length of the value
    print("Your name is long enough.")

    if len(name) > 15:
        print("That is way too long.")
    else:
        print(f"Welcome {name}")

name = input("What is your name?")

if len(name) > 3:
    if len(name) < 10:
        if len(name) == 4:
            print('Perfect length!')
        else:
            print("it's an okay length.")
        print(f"Welcome {name}")
    else:    
    print("That's way to long partner!")

else:
    print('%s is too few characters.' % length)
    #print(f' {length} is too few characters.') #or alt pattern
