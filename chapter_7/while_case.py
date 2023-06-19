# 7-1
car = input("Which kind of car do you want to rent?")
print(f"\nLet me see if I can find you a {car.title()}.")

# 7-2
number = input("How many people will dine?")
number = int(number)

if number > 8:
    print("There are no empty tables.")
else:
    print("There are empty tables.")

# 7-3
num = input("Enter a number, and I'll tell you if it's an integer multiple of 10:")
num = int(num)

if (num % 10) == 0:
    print(f"\nThe number {num} is an integer multiple of 10.")
else:
    print(f"\nThe number {num} is not an integer multiple of 10.")

# 7-4
prompt = "\nPlease tell me which ingredients do you want to add?"
prompt += "\n(Enter 'quit' if you finished)."

ingredients = ""
while ingredients != 'quit':
    ingredients = input(prompt)
    if ingredients != 'quit':
        print(f"The pizza will add {ingredients.title()}!")

# 7-5
tip = ""
while tip != 'quit':
    tip = input("Please tell me how old are you?")
    age = int(tip)
    if tip != 'quit':
        if age < 3:
            print("\nYou are free to see a movie!")
        elif (age >= 3 and age < 12):
            print("\nYou need pay $10 to see a movie!")
        elif age > 12:
            print("\nYou need pay $15 to see a movie!")

# 7-8
sandwich_orders = ['kfc', 'm', 'pizza']
finished_sandwiches = []
while sandwich_orders:
    sandwich_ordering = sandwich_orders.pop()

    print(f"I made your {sandwich_ordering.title()} sandwich. ")
    finished_sandwiches.append(sandwich_ordering)

print("\nThe following sandwiches have been finished:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# 7-9
sandwich_orders = ['pastrami', 'kfc', 'pastrami', 'm', 'pizza', 'pastrami']
finished_sandwiches = []
print("Pastrami sandwich has been sold out!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    sandwich_ordering = sandwich_orders.pop()

    print(f"I made your {sandwich_ordering.title()} sandwich. ")
    finished_sandwiches.append(sandwich_ordering)

print("\nThe following sandwiches have been finished:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# 7-10
places = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    places[name] = place

    repeat = input("Would you like to let another person respond?(yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("\n---Poll Results ---")
for name, place in places.items():
    print(f"{name} would like to visit {place}.")


