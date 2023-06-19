class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.lastname = last_name
        self.salary = salary

    def give_raise(self, number=5000):
        self.salary += number

