# 1. hello-you

name = input("What is your name?\n")
num  = len(name)
print(f"Hello, {name}!")

print(f"Your name has {num} letters in it. Awesome!")

# 2. HELLO-YOU

name = input("WHAT IS YOUR NAME?\n")
num  = len(name)
print(f"HELLO, {name.upper()}!")

print(f"YOUR NAME HAS {num} LETTERS IN IT. AWESOME!")

# 3. Madlib

print("Please fill in the blanks.\n __(name)__'s favorite __(subject)__ in school.")
name = input("What is your name?\n")
subject = input("What is your favorite subject in school?\n")
print(f"{name}'s favorite subject in school is {subject}.")

# 4. Day of the Week [preferred]

day_num = int(input("How many days into this week are we? Enter 0-6\n"))
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print(days[day_num])

# Alternate [more complicated]

day = int(input('Day (0-6)?'))
if day == 0:
    print("Sunday")
elif day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")

# 5. Work or Sleep In?

day - int(input("(0-6)?"))

# if day > 0 and day < 6: # debug - never goes to else because 0<6 and 6>0
# if day > 0 or day < 6: # debug - not going to else
if day == 0 or day == 6:
    print("Go to work!")
else:
    print("Sleep in!")

day = int(input('Day (0-6)? ')) # Marcus De La Garza Slack msg
if day == 0 or day == 6:
    print("Sleep in!")
else:
    print("Go to work!")

day = int(input("What day is today using (0-6) in place of the day?\n"))
if day == 0:
    print("Sleep in!")
elif day == 6:
    print("Sleep in!")
elif day == 1 or 2 or 3 or 4 or 5:
    print("Go to work!")

#6. Celsius to Fahrenheit

celsius - int(input("What is the temperature in degrees C?"))
fahr = (celsius * 9/5) + 32
print("%i F" % (fahr))
# print(int(temp * 9/5) + 32) + str(F)) # How to get this to concatenate correctly?

# 7. Looping from 1 to 10



# 8. n to m



# 9. Print a Square




#  10. Print a Square II


