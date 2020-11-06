# try:
#     if 2 > "3"
#         print("Never prints.")
# except typeError:
#     print("You did something wrong with the type.")
# except ZeroDivisionError:
#     print("You tried to divide by 0")


try:
    print(100 / int(input("Give me a number")))
except ZeroDivisionError:
    print("You tried to divide by 0")
except TypeError:
    print("You did something wrong with the type.")
except ValueError:
    print("You didn't give a number.")


my_num = input("Give me a number")
    print(type(my_num))
try:
    my_num = int(my_num)
    print(100 / my_num)
    print(type(my_num))
except ZeroDivisionError:
    print("You tried to divide by 0")
except TypeError:
    print("You did something wrong with the type.")
except ValueError:
    print("You didn't give a number.")

print(type(my_num))



