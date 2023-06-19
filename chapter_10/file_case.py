# 10-1
filename = 'python_learn/Python_Crash_Course/chapter_10/learning_python.txt'

with open(filename) as file_object:
    txt = file_object.read()
    lines = file_object.readlines()
    for line in lines:
        print(line)

txt_all = ''
for line in lines:
    txt_all += line.rstrip()

print(txt.rstrip())
print(txt_all)

# 10-2
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        line_replaced = line.replace('Python', 'C')
        print(line_replaced)

# 10-3
filename = 'guest.txt'

with open(filename, 'w') as file_object:
    name = input("Please tell me your name: ")
    file_object.write(name+'\n')

# 10-4
filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    active = True
    while active:    
        name = input("Please tell me your name: ")
        if name == 'q':
            active = False
        else:
            print(f"Hello, {name.title()}!")
            file_object.write(name+'\n')

# 10-5
filename = 'reason_python.txt'

with open(filename, 'w') as file_object:
    active = True
    while active:    
        reason = input("Please tell me why you like Python: ")
        if reason == 'q':
            active = False
        else:
            print("Continue or enter q to quit")
            file_object.write(reason+'\n')

# 10-6
num_1 = input("Please enter the first number to add: ")
num_2 = input("Please enter the second number to add: ")

try:
    answer = int(num_1) + int(num_2)
except ValueError:
    print("Please enter number not word!")
else:
    print(answer)

# 10-7
while True:
    num_1 = input("Please enter the first number to add: ")
    if num_1 == 'q':
        break  
    num_2 = input("Please enter the second number to add: ") 
    if num_2 == 'q':
        break
    try:
        answer = int(num_1) + int(num_2)
    except ValueError:
        print("Please enter number not word!")
    else:
        print(answer)

# 10-8
filenames = ['cats.txt', 'pigs.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(f"Sorry. There is not a file {filename}!")

# 10-9
filenames = ['cats.txt', 'pigs.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        pass

# 10-10
filenames = ['alice.txt', 'qwe.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
            number = contents.count('the ')
            print(f"There are {number} 'the' words in this file!")
    except FileNotFoundError:
        print(f"There is not a file {filename}!")


# 10-11
# write favorite number
import json

number = input("Enter your favorite number: ")
filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(number,f)

# read favorite number 
import json

filename = 'favorite_number.json'
with open(filename) as f:
    number = json.load(f)
print(f"I kown your favorite number! It's {number}!")
