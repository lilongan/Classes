# age = input("How old are you?\n") #blocked 1-5, Ctrl/
# if int(age) >= 21:
#     print("You are old enough.")
# else:
#     print("you are not old enough.")

age = int(input("How old are you?\n"))

if age == 21:
    print("You are a great age to party.")
elif age > 37:
    print("Your getting up there in age!")
elif age >= 21:
    print("You are old enough.")
else:
    print("You are not old enough.")

