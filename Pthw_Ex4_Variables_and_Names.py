cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
# Cars_not_driven == 70
cars_not_driven = cars - drivers
cars_driven = drivers
# There are 30 drivers, which is directly equivalent to cars. Each car has an assumed capacity of 4, thus how many passengers as denoted by carpool_capacity will be 120.
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# All the variables below have been previously established
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
