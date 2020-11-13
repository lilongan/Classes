cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars-drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

console.log("There are", cars, "cars available.")
console.log("There are only", drivers, "drivers available.")
console.log("There will be", cars_not_driven, "empty cars today.")
console.log("We can transport", carpool_capacity, "people today.")
console.log("We have", passengers, "to carpool today.")
console.log("We need to put about", average_passengers_per_car, "in each car.")
// Both 1-15 && 17-31 work okay.
cars = 100
spaceInEachCar = 4.0
drivers = 30
passengers = 90
carsNotDriven = cars-drivers
carsDriven = drivers
carpoolCapacity = carsDriven * spaceInEachCar
averagePassengersPerCar = passengers / carsDriven

console.log("There are", cars, "cars available.")
console.log("There are only", drivers, "drivers available.")
console.log("There will be", carsNotDriven, "empty cars today.")
console.log("We can transport", carpoolCapacity, "people today.")
console.log("We have", passengers, "to carpool today.")
console.log("We need to put about", averagePassengersPerCar, "in each car.")
