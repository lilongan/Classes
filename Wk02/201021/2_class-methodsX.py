# Using our vehicle class from the previous lesson, add a speed, top_speed, 
# position, and acceleration attribute.

#     Speed and position should start at 0, top_speed and acceleration 
#       are numbers.
#     Add a class method called move. When the move method is called have 
#       the position increase by the speed of the car.
#     Add a class method called accelerate and using the very simplified 
#       equation to have the vehicle accelerate when the accelerate method 
#       is called on that instance:

#  speed = speed + acceleration

#     In the accelerate method, do not allow the vehicle to pass the top 
#       speed.
#     Modify the instances of the vehicles to include acceleration and 
#       top speed when you instance the vehicles.
#     Using a while loop and assuming each iteration of the loop is a 
#       'second' have the vehicles 'race' by accelerating as much as 
#       possible on a drag strip for 20, 40, and 60 seconds to see who wins.
#     (challange) Instead of racing for a timeframe, make the race 
#       different distances. Position can be considered in meters.
# -- -- -- 
class Vehicle:
    def __init__(self,category,color,top_speed,acceleration,wheels=4):
        print(self)
        print("You created a new instance of Vehicle.")
        self.category = category
        self.color = color
        self.top_speed = top_speed
        self.acceleration = acceleration
        self.speed = 0
        self.position = 0
        self.wheels = wheels

    def move(self):
        self.accelerate()
        self.position += self.speed

    def accelerate(self):
        self.speed += self.acceleration
        if self.speed > self.top_speed:
            self.speed = self.top_speed

sport = Vehicle("Porche Boxster","sport","metalic green",190,6)

all_cars = {
"Porche":Vehicle("sport","metalic green",100,4),
"Ford":Vehicle("truck","white",120,4),
"Dodge":Vehicle("minivan","bronze",110,3),
"Harley":Vehicle("motorcycle","burgandy",180,5)
}

print("20 Second run!")

for i in range(20):
    for car_name in all_cars:
        all_cars[car_name].move

for car_name in all_cars:
    print(f" {car_name} - {all_cars[car_name].position}")






# sport = Vehicle("Porche Boxster","sport","metalic green",0,0,190,60)
# truck = Vehicle("Ford","truck","white",0,0,120,40)
# minivan = Vehicle("Dodge","minivian","bronze",0,0,110,30)
# motorcycle = Vehicle("Harley","motorcycle","burgandy",0,0,180,50,2)

# print(f"Wow, you have a {sport.make} {sport.category} that is {sport.color} with {sport.wheels}.")
# print(f"Wow, you have a {truck.make} {truck.category} that is {truck.color} with {truck.wheels}.")
# print(f"Wow, you have a {minivan.make} {minivan.category} that is {minivan.color} with {minivan.wheels}.")
# print(f"Wow, you have a {motorcycle.make} {motorcycle.category} that is {motorcycle.color} with {motorcycle.wheels}.")

# sport = Vehicle("Porche Boxster")
# truck = Vehicle("Ford")
# nimivan = Vehicle("Dodge")
# motorcycle = Vehicle("Harley")

# print(self.make)
# print(self.category)
# print(self.color)
# print(self.speed)
# print(self.position)
# print(self.top_speed)
# print(self.acceleration)
# print(self.wheels)

# hero = Mob("Sir Barksalot",30,1)
# bad_guy = Mob("EvilMcEvil",10,3)
# bad_guy.attack(hero)

# -- -- -- 
