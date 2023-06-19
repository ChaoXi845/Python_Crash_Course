# This is a exercise about list
# 3-4
invite_list = ['Zhu Liang', 'Huang Zhikai', 'Jiang Peijie']
print("Hello " + invite_list[0].title() + ", I am your father!")
print("Hello " + invite_list[1].title() + ", I am your father!")
print("Hello " + invite_list[2].title() + ", I am your father!")

# 3-5
invite_list = ['Zhu Liang', 'Huang Zhikai', 'Jiang Peijie']
print("Because " + invite_list[0].title() + "is my grandson, So he should be removed from this list!")
invite_list[0] = 'Zhang Jiaowei'
print(invite_list)

# 3-6
invite_list = ['Zhu Liang', 'Huang Zhikai', 'Jiang Peijie']
invite_list.insert(0, 'Yang Hao')
invite_list.insert(2, 'Liu Shuainian')
invite_list.append('Xiu Runfa')
print(invite_list)

# 3-7
print("Go out, " + invite_list.pop() + "!")
print("Go out, " + invite_list.pop() + "!")
print("Go out, " + invite_list.pop() + "!")
print("Go out, " + invite_list.pop() + "!")
print("Come in, " + invite_list[0] + "!")
print("Come in, " + invite_list[1] + "!")
del invite_list[0]
del invite_list[0]
print(invite_list)

# 3-8
name_school = ['NUS', 'NTU', 'TJU', 'MIT', 'Standford']
print(name_school)

sorted(name_school)
print(name_school)

sorted(name_school, reverse=True)
print(name_school)

name_school.reverse()
print(name_school)

name_school.reverse()
print(name_school)

name_school.sort()
print(name_school)

name_school.sort(reverse=True)
print(name_school)

# 3-9
name_school.sort(reverse=True)
len(name_school)
print(len(name_school))

