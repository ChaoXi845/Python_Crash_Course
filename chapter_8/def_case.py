# 8-1
def display_message():
    print("I am learning how to use Python and Markdown!")

display_message()

# 8-2
def favorite_book(name):
    """ This is a def to learn parameter and argument """ 
    print(f"One of my favorite books is {name.title()}.")

favorite_book('alice in wonderland')

# 8-3
def make_shirt(size, logo):
    print(f"Please give me a {size.upper()} T-shirt, and print a {logo} on it!")

make_shirt('M', 10)
make_shirt(logo=24, size='M')

# 8-4
def make_shirt(size='L', logo='I love Python'):
    print(f"a {size.upper()} T-shirt with {logo}.")

make_shirt()
make_shirt(size='M')
make_shirt(logo='I hate Python')

# 8-5
def describe_city(name='reykjavik', country='iceland'):
    print(f"{name.title()} is in {country.title()}.")

describe_city()
describe_city(name='singapore', country='singapore')
describe_city(name='shanghai', country='china')

# 8-6
def city_country(city, country):
    message = city.title() + ", " + country.title()
    return message

message_1 = city_country('guiyang', 'china')
print(message_1)
message_2 = city_country('shanghai', 'china')
print(message_2)
message_3 = city_country('singapore', 'singapore')
print(message_3)

# 8-7
def make_album(singer, name, number=None):
    album = {'singer': singer, 'name': name}
    if number:
        album['number'] = number
    
    return album

album_1 = make_album('Eason Chan', 'H')
print(album_1)
album_2 = make_album('Eason Chan', '黑白灰')
print(album_2)
album_3 = make_album('Eason Chan', '上五楼的快活', number=12)
print(album_3)

# 8-8 
def make_album(singer, name, number=None):
    album = {'singer': singer, 'name': name}
    if number:
        album['number'] = number
    
    return album

while True:
    print("\nPlease tell me some information about the album: ")
    print("(enter 'q' at any time to quit)")

    album_singer = input("Singer: ")
    if album_singer == 'q':
        break

    album_name = input("Name: ")
    if album_name == 'q':
        break

    album_number = input("Number: ")
    if album_number == 'q':
        break

    favorite_album = make_album(album_singer, album_name, album_number)
    print(favorite_album)

# 8-9 
def show_messages(messages):
    for message in messages:
        print(message)

msg = ['qwe', 'asd', 'zxc']
show_messages(msg)

# 8-10
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages,sent_messages):
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)
    print(sent_messages)


msg = ['qwe', 'asd', 'zxc']
sent_msg = []
show_messages(msg)
send_messages(msg, sent_msg)

# 8-11
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages,sent_messages):
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)
    print(sent_messages)


msg = ['qwe', 'asd', 'zxc']
sent_msg = []
show_messages(msg)
send_messages(msg[:], sent_msg)
print(msg)
print(sent_msg)

# 8-12
def topping_sandwich(*toppings):
    print("Making a sandwich with following toppings: ")
    for topping in toppings:
        print(f"-{topping}")

topping_sandwich('pepperni')
topping_sandwich('mushrooms', 'green peppers', 'extra cheese')

# 8-13
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('zongrui', 'li',
                             location='guiyang',
                             field='robotics',
                             country='china')
print(user_profile)

# 8-14
def make_car(builder, type, **car_info):
    car_info['builder'] = builder
    car_info['type'] = type
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)