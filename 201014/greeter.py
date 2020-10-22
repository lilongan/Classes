# 201014 Lesson how-do-i-make-choices-based-on-the-user-s-input

greeting = "Hello %s, it is very nice to meet you and your friend %s!"

name_of_user = input("What is your name? ")
length_of_name = len(name_of_user)
if length_of_name > 0:
    name_of_friend = input("What is your friend's name? ")
    print(greeting % (name_of_user, name_of_friend))

    greeting = "Hello %s, it is very nice to meet you and your friend %s!"

name_of_user = input("What is your name? ")
length_of_name = len(name_of_user)
if length_of_name > 0:
    name_of_friend = input("What is your friend's name? ")
    print(greeting % (name_of_user, name_of_friend))
else:
    print("OK, I'll ask again some other time.")

    greeting = "Hello %s, it is very nice to meet you and your friend %s!"

name_of_user = input("What is your name? ")
length_of_name = len(name_of_user)
if length_of_name > 0:
    name_of_friend = input("What is your friend's name? ")
    print(greeting % (name_of_user, name_of_friend))
else:
    pass

greeting = "Hello %s, it is very nice to meet you and your friend %s!"

name_of_user = input("What is your name? ")
length_of_name = len(name_of_user)
if length_of_name > 10:
    print("That's a really long name!")
elif length_of_name > 0:
    name_of_friend = input("What is your friend's name? ")
    length_of_friend_name = len(name_of_friend)
    if length_of_friend_name > 0:
        print(greeting % (name_of_user, name_of_friend))
else:
    print("OK, I'll ask again some other time.")

greeting = "Hello %s, it is very nice to meet you and your friend %s!"

name_of_user = input("What is your name? ")
name_of_friend = input("What is your friend's name? ")

length_of_name = len(name_of_user)
length_of_friend_name = len(name_of_friend)

if length_of_name > 0 and length_of_friend_name > 0:
    print(greeting % (name_of_user, name_of_friend))
else:
    print("OK, I'll ask again some other time.")

    greeting = "Hello %s, it is very nice to meet you and your friend %s!"

name_of_user = input("What is your name? ")
name_of_friend = input("What is your friend's name? ")

length_of_name = len(name_of_user)
length_of_friend_name = len(name_of_friend)

if length_of_name == 0 or length_of_friend_name == 0:
    print("OK, I'll ask again some other time.")
else:
    print(greeting % (name_of_user, name_of_friend))

    False and print('hey')
# Does not run the print function

True and print('hey')
# Prints "hey"

False or print('hey')
# Prints "hey"

True or print('hey')
# Does not run the print function

# end assignment notes on greeter