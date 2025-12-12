# Patrice Moracchini
# CSD-325
# test_cities.py
# this program tests the city_functions.py file

import unittest #imports the unittest module
class TestCityFunctions(unittest.TestCase): # creates a class to test city functions
    def test_city_country(self): # test for city_country function
        from city_functions import city_country
        self.assertEqual(city_country("Santiago", "Chile"), "Santiago, Chile") # test with just city and country
        self.assertEqual(city_country("Paris", "France"), "Paris, France") # test with just city and country
        self.assertEqual(city_country("Rome", "Italy"), "Rome, Italy") # test with just city and country
        # the test will pass only if the extra parameters are optional in the function
if __name__ == "__main__":
    unittest.main()