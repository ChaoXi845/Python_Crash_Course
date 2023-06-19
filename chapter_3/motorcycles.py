# This is a tutorial about how to modify list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati') # append() is a function to add a new element at the end of the list
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') # insert() is a function to add a new element at the position you decided
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0] # del is a function to delete a element which you choose in the list
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop() # pop() is a function like Cut
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive) # remove is a function to remove the element you kown the value
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")