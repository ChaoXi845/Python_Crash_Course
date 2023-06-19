# This is the exercise about how to use if
# 5-1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict True.")
print(car == 'audi')

# 5-2
# conditional_tests.py

# 5-3
alien_color = 'green'
if alien_color == 'green':
    print("You get 5 points!")
if alien_color != 'green':
    print("You are Wrong!")

# 5-4
if alien_color == 'green':
    print("You get 5 points!")
else:
    print("You get 10 points!")

# 5-5
if alien_color == 'green':
    print("You get 5 points!")
elif alien_color == 'yellow':
    print("You get 10 points!")
elif alien_color == 'red':
    print("You get 15 points!")

# 5-6
age = 20
if age < 2:
    print("You are a baby!")
elif (age >= 2) and (age < 4):
    print("You are learnning how to walk.")
elif (age >= 4) and (age < 13):
    print("You are a child!")
elif (age >= 13) and (age < 20):
    print("You are an adolescent!")
elif (age >= 20) and (age < 65):
    print("You are an adult!")
elif age >= 65:
    print("You are an old man!")

# 5-7
favorite_fruits = ['watermelo', 'apple', 'banana']
if 'watermelo' in favorite_fruits:
    print("You really like watermelo!")
elif 'apple' in favorite_fruits:
    print("You really like apple!")
elif 'banana' in favorite_fruits:
    print("You really like banana!")

# 5-8
user_list = ['admin', 'tide', 'chaoxi', 'zhu liang', 'yang hao']
for user in user_list:
    if user == 'admin':
        print("Hello, " + user.title() + ", would you like to see a status report?")
    else:
        print("Hello, " + user.title() + ", thank you for logging in again.")

# 5-9
user_list = []
if not user_list:
    print("We need to find some users!")

# 5-10
current_users = ['admin', 'tide', 'chaoxi', 'zhu liang', 'yang hao']
new_users = ['zhao jiawei', 'Tide', 'liu shuainian', 'yang hao', 'zhang zijie']
current_users_lower = [current_user.lower() for current_user in current_users]
for user in new_users:
    if user.lower() in current_users:
        print("The name has been used! Please use a new one!")
    else:
        print("Congratulation! You are the new user!")

# 5-11
number_list = [i for i in range(1,10)]
for i in number_list:
    if i == 1:
        print(str(i) + 'st')
    elif i == 2:
        print(str(i) + 'nd')
    elif i == 3:
        print(str(i) + 'rd')
    else:
        print(str(i) + 'th')