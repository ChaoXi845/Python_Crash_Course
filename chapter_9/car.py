class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can not roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer += miles
        
my_new_car = Car('audi', 'a4', '2023')
print(my_new_car.get_descriptive_name())

# my_new_car.odometer = 23
my_new_car.update_odometer(32)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()