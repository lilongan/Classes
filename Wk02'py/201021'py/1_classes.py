# Create first "class"

# class Person:
#     pass
# for i in range(3):
#     pass

# Clint = Person()
# Anna = Person()

# print(Clint)

# class Person:
#     def __init__(self): # "self" is alwasy 1st perameter in python3
#         print("You created a new instance of Person.")

# Clint = Person()
# Anna = Person()

# print(Clint)

# class Person:
#     def __init__(self):
#         print(self)
#         print("You created a new instance of Person.")

# Clint = Person()
# Anna = Person()

# print(Clint)

# class Person:
#     def __init__(foo):
#         print(foo)
#         print("You created a new instance of Person.")

# Clint = Person()
# Anna = Person()

# print(Clint)

# class Person:
#     def __init__(self):
#         print(self)
#         print("You created a new instance of Person.")
#         self.name = "Clint"
#         self.age = 38

# Clint = Person()
# Anna = Person()

# print(Clint.age)
# print(Anna.age)

# class Person:
#     def __init__(self,name,age):
#         print(self)
#         print("You created a new instance of Person.")
#         self.name = name
#         self.age = age

# Clint = Person("Clint",38)
# Anna = Person("Anna",37)

# print(Clint.age)
# print(Anna.age)

# class Person:
#     def __init__(self,name,age):
#         print(self)
#         print("You created a new instance of Person.")
#         self.name = name
#         self.age = age

# Clint = Person("Clint",38)
# Anna = Person("Anna",37)

# print(f"Wow {Clint.name} you are {Clint.age} years old.")
# print(f"Wow {Anna.name} you are {Anna.age} years old.")

class Person:
    def __init__(self,name,age, height="normal"):
        print(self)
        print("You created a new instance of Person.")
        self.name = name
        self.age = age
        self.height = height

Clint = Person("Clint",38,"short")
Anna = Person("Anna",37)

print(f"Wow {Clint.name} you are {Clint.age} years old and {Clint.height}.")
print(f"Wow {Anna.name} you are {Anna.age} years old and {Anna.height}.")
print(Clint.height)
print(Anna.height)

