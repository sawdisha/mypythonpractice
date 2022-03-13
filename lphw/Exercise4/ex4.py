# assigning value to variable cars
cars = 100
# assigning floating point value to variable space_in_a_car
space_in_a_car = 4.0
# assigning number of available drivers count to variable drivers.
drivers = 30
# Assigning number of available passengers for the day to variable passengers
passengers = 90
# calulating cars not driven and assigning result to the variable cars_not_driven
cars_not_driven = cars - drivers
# Assigning value to the variable cars cars_driven
cars_driven = drivers
# calulating carpool capacity by multiplying cars_driven by space_in_a_car and assigning result to the variable carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# calulating average passengers that should travel per cars so that all drivers have equal number of clients.
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers,"drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")
