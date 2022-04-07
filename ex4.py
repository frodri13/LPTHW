# amount of cars
cars = 100
# how many people can enter it
space_in_a_car = 4.0
# total num of drivers
drivers = 30
# total amount of passengers
passengers = 90
# num of cars that have not been driven
cars_not_driven = cars - drivers
# the num of cars driven can only be equal to the amount of drivers available
cars_driven = drivers
# How many people in total can we fit into all of the cars available
carpool_capacity = cars_driven * space_in_a_car
# The avg of passengers is calculated by dividing the num of passengers by the cars that we have available to drive
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "divers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")