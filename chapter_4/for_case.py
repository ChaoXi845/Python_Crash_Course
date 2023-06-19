# This is a exercise about for
# 4-1
pizzas = ['KFC', 'M', 'Pizza Hut']
for pizza in pizzas:
    print("I like " + pizza + " pizza!")
print("I really love pizza!") 

# 4-2
animals = ['dog', 'cat', 'fish']
for animal in animals:
    print(animal)
    print("A " + animal + " would mkae a great pet\n")
print("Any of these animals would make a great pet!")

# 4-3
for i in range(1, 21):
    print(i)

# 4-4
num_list = [i for i in range(1, 1000001)]
#for i in num_list:
#    print(i)
# print(num_list)

# 4-5
num_list = [i for i in range(1, 1000001)]
print(min(num_list))
print(max(num_list))
print(sum(num_list))

# 4-6
even_list = [i for i in range(1, 21, 2)]
print(even_list)
for i in even_list:
    print(i)

# 4-7
tri_list = [i for i in range(3, 31, 3)]
print(tri_list)
for i in tri_list:
    print(i)

# 4-8
cube = []
for i in range(1, 11):
    cube.append(i**3)
print(cube)

# 4-9
cube_list = [value**3 for value in range(1, 11)]
print(cube_list)
for i in cube_list:
    print(i)

# 4-10
cube_list = [value**3 for value in range(1, 11)]
print("The first three items in the list are:")
for i in cube_list[:3]:
    print(i)

print("\nThree items from the middle of the list are:")
mid_index = len(cube_list) // 2
for i in cube_list[mid_index - 1:mid_index + 2]:
    print(i)

print("\nThe last three items in the list are:")
for i in cube_list[-3:]:
    print(i)

# 4-11
friend_pizzas = pizzas[:]
pizzas.append('Sariya')
friend_pizzas.append('Subway')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

# 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]


my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)

# 4-13
foods = ('fish', 'seafood', 'noodles', 'rice', 'chicken')
print("Original food list:")
for food in foods:
    print(food)

print("\nModified food list:")
foods = ('dumpling', 'seafood', 'noodles', 'rice', 'chicken')
for food in foods:
    print(food)
