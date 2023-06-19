# This is a tutorial how to organize the list

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # sort() is a function about modify the queue of the list permanently
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) # hypeperemeter reverse=True will make the queue reverse sort
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the sorted list:")
print(sorted(cars))
print(sorted(cars, reverse=True))

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() # reverse() is a function to reverse the list permanently
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars) # len() is a function to get the length of list
print(len(cars))
