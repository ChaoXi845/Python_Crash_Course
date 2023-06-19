file_path = 'G:/Tide/python_work/python_learn/Python_Crash_Course/chapter_10/pi_digits.txt'

with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip()) 

