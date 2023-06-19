# from car import Car

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer = 23
# my_new_car.read_odometer()

import electric_car

my_beetle = electric_car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = electric_car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

