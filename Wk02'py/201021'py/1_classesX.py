# Create a program that has a class named Vehicle.

#     Make the Vehicle have a 'category' which can be anything like, minivan.wh    truck, motorcycle, minivan.
#     Make the Vehicle class have 'wheels' as an attribute.
#     Make the Vehicle class have 4 as the default value for the class.
#     Create 5 different instances of the class with at least one being a motorcycle.

# class Vehicle:
#     def __init__(category,color,wheels="4"):
#         print(self)
#         print("You created a new instance of Vehicle.")
#         self.category = category
#         self.color = color
#         self.wheels = wheels

# Porche_Boxster = Vehicle("Porche Boxster","metalic green","sport")
# Ford = Vehicle("Ford","white","truck")
# Dodge = Vehicle("Dodge","bronze","minivan")
# Harley = Vehicle("Harley","burgandy","2")

# print(f"Wow, you have a {Porche_Boxster.category} that is {Porche_Boxster.color} with {Porche_Boxster.wheels}.")
# print(f"Wow, you have a {Ford.category} that is {Ford.color} with {Ford.wheels}.")
# print(f"Wow, you have a {Dodge.category} that is {Dodge.color} with {Dodge.wheels}.")
# print(f"Wow, you have a {Harley.category} that is {Harley.color} with {Harley.wheels}.")
# -- -- -- 
class Vehicle:
    def __init__(self,category,color,wheels=4):
        print(self)
        print("You created a new instance of Vehicle.")
        self.category = category
        self.color = color
        self.wheels = wheels

sport = Vehicle("sport","metalic green")
truck = Vehicle("truck","white")
minivan = Vehicle("minivian","bronze")
motorcycle = Vehicle("motorcycle","burgandy",2)

# sport = Vehicle("Porche Boxster")
# truck = Vehicle("Ford")
# nimivan = Vehicle("Dodge")
# motorcycle = Vehicle("Harley")

print(f"Wow, you have a {sport.category} that is {sport.color} with {sport.wheels}.")
print(f"Wow, you have a {truck.category} that is {truck.color} with {truck.wheels}.")
print(f"Wow, you have a {minivan.category} that is {minivan.color} with {minivan.wheels}.")
print(f"Wow, you have a {motorcycle.category} that is {motorcycle.color} with {motorcycle.wheels}.")
# -- -- -- 
