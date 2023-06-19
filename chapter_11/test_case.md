# Chapter 11 Test

## 11-1  

city_functions.py

```python
def city(city_name, country_name):
    city_country = f"{city_name.title()}, {country_name.title()}"
    return city_country
```

test_cities.py

```python
import unittest
from city_functions import city

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        cities = city('shanghai', 'china')
        self.assertEqual(cities, 'Shanghai, China')

if __name__ == "__main__":
    unittest.main()

```

## 11-2

city_functions.py

```python
def city(city_name, country_name, population=''):
    if population:
        city_country = f"{city_name.title()}, {country_name.title()} - population {population}"
    else:
        city_country = f"{city_name.title()}, {country_name.title()}"
    return city_country

```

test_cities.py

```python
import unittest
from city_functions import city

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        city_info = city('shanghai', 'china')
        self.assertEqual(city_info, 'Shanghai, China')

    def test_city_country_population(self):
        city_info = city('shanghai', 'china', 20000000)
        self.assertEqual(city_info, 'Shanghai, China - population 20000000') 
if __name__ == "__main__":
    unittest.main()

```

## 11-3

employee_class.py

```python
class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.lastname = last_name
        self.salary = salary

    def give_raise(self, number=5000):
        self.salary += number

```

test_employee.py

```python
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


```
