# This is an exercise about how to use dictionary
# 6-1
person = {
    'first_name': 'Zongrui',
    'last_name': 'Li',
    'age': 23,
    'city': 'Singapore'
}
print(person)

# 6-2
favorite_number = {
    'Tide': 8,
    'Zhu Liang': 2,
    'Huang Zhikai': 7,
    'Zhao Jiawei': 10,
    'Yang Hao': 24
}
print(favorite_number)

# 6-3
word_python = {
    '字典': '字典是一系列键-值对。',
    '元组': '元组是不可变的列表。',
    '列表': '列表是一系列按特定顺序排列的元素。'
}

# 6-4
for key, value in word_python.items():
    print(key + ': ' + value)

# 6-5
rivers = {
    'nile': 'egypt',
    'rhine': 'switzerland',
    'chang': 'china'
}

for river, country in rivers.items():
    print('The ' + river.title() + ' runs through ' + country.title())

# 6-6
# 6-7
person_0 = {
    'first_name': 'Zongrui',
    'last_name': 'Li',
    'age': 23,
    'city': 'Singapore'
}

person_1 = {
    'first_name': 'Hao',
    'last_name': 'Yang',
    'age': 23,
    'city': 'Baiyin'
}

person_2 = {
    'first_name': 'Liang',
    'last_name': 'Zhu',
    'age': 23,
    'city': 'Changzhou'
}

persons = [person_0, person_1, person_2]

for person in persons:
    print(person)

# 6-8
pet_0 = {
    'kind': 'dog',
    'master': 'Li'
}

pet_1 = {
    'kind': 'cat',
    'master': 'Yang'
}

pet_2 = {
    'kind': 'akai',
    'matser': 'Zhu'
}

pets = [pet_0, pet_1, pet_2]
for pet in pets:
    print(pet)

# 6-9
favorite_places = {
    'Li': ['Jinsha', 'Shanghai', 'Singapore'],
    'Yang': ['Baiyin', 'Hengshui', 'Shanghai'],
    'Zhu': ['Changzhou', 'Shanghai']
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are: ")
    for place in places:
        print(f' {place}')

# 6-10
favorite_number = {
    'Tide': [8, 24],
    'Zhu Liang': [2, 10],
    'Huang Zhikai': [7, 14],
    'Zhao Jiawei': [10, 58],
    'Yang Hao': [24,100]
}
for person, numbers in favorite_number.items():
    print(f"{person}'s favorite numbers are: ")
    for number in numbers:
        print(number)

# 6-11
cities = {
    'guiyang': {'country': 'china', 'population': 5987018},
    'shanghai': {'country': 'china', 'population': 24894300},
    'singapore': {'country': 'sinagpore', 'population': 5866100}
}

for city, fact in cities.items():
    print(f"{city.title()} is located in {fact['country'].title()}, and the population is {fact['population']}.")