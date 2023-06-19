import unittest
from employee_class import Employee

class EmployeeTest(unittest.TestCase):

    def setUp(self):
        firstname = 'zongrui'
        lastname = 'li'
        salary = 2000
        self.info = Employee(firstname, lastname, salary)

    def test_give_default_raise(self):
        self.info.give_raise()
        self.assertEqual(self.info.salary, 7000)

    def test_give_custom_raise(self):
        self.info.give_raise(6000)
        self.assertEqual(self.info.salary, 8000)

if __name__ == '__main__':
    unittest.main()
        
