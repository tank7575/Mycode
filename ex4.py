cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
#equal then subratcting
cars_not_driven = cars - drivers
#equal too
cars_driven = drivers
#equal too and multcation
carpool_capacity = cars_driven * space_in_a_car
#equal too then divesen
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers_available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
