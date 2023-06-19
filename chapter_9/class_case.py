# 9-1
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is openning!")

restaurant_1 = Restaurant('guizhoufandian', 'qiancai')
print(restaurant_1.restaurant_name)
print(restaurant_1.cuisine_type)

# 9-2
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

# 9-3
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}!")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

user_1 = User('zhu', 'liang')
user_2 = User('huang', 'zhikai')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

# 9-4
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is openning!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment_number):
        self.number_served += increment_number

restaurant_2 = Restaurant('guizhoufandian', 'qiancai')
print(restaurant_2.number_served())
restaurant_2.number_served = 10
print(restaurant_2.number_served())
restaurant_2.set_number_served(15)
print(restaurant_2.number_served())
restaurant_2.increment_number_served(10)
print(restaurant_2.number_served())

# 9-5
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}!")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user_1 = User('zhu', 'liang')
user_2 = User('huang', 'zhikai')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

print(user_1.login_attempts)

user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)

# 9-6 
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is openning!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment_number):
        self.number_served += increment_number

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['a', 'b', 'c']
    
    def show_flavors(self):
        print("The flavors are following: ")
        for flavor in self.flavors:
            print(flavor.title())

icecream_1 = IceCreamStand('guizhou', 'qian')
icecream_1.show_flavors()

# 9-7
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}!")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("The following is the admin's privileges: ")
        for privilege in self.privileges:
            print(privilege.title())

user_9 = Admin('li', 'zongrui')
user_9.show_privileges()

# 9-8
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}!")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("The following is the admin's privileges: ")
        for privilege in self.privileges:
            print(privilege.title())

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
        
user_9 = Admin('li', 'zongrui')
user_9.privileges.show_privileges()

# 9-9
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("The car's gas tank has been filled!")

class Battery:

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 60
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("The car does not need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()
my_bwm = Car('bwm', 'z4', 2023)
my_bwm.fill_gas_tank()


# 9-13
from random import randint
class Die:
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

die_6 = Die(6)
print(die_6.roll_die())

die_10 = Die(10)
print(die_10.roll_die())

die_20 = Die(20)
print(die_20.roll_die())

# 9-14
from random import choice

reward = [1, 'a', 2, 'b', 3, 'c', 4, 'd',5 ,6, 7, 8, 9, 10]

one = choice(reward)
if one == ('a' or 'b' or 1 or 2):
    print("You get the reward!")
else:
    print("Sorry but Thanks!")

# 9-15
from random import choice

reward = [1, 'a', 2, 'b', 3, 'c', 4, 'd',5 ,6, 7, 8, 9, 10]
my_ticket = []
active = True
while active:

    one = choice(reward)
    my_ticket.append(one)
    if one == ('a' or 'b' or 1 or 2):
        active = False
        print("You get the reward!")
        print(f"You have bought {len(my_ticket)} tickets!")
    else:
        print("Sorry but Thanks!")
