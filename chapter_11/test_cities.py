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