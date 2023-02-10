#!/usr/bin/python3

import models
import unittest
import pep8
from models.city import City
from datetime import datetime

class TestCity(unittest.TestCase):
    def set_up(self):
        self.city = City()

    def city_init(self):
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city.sate_id, str)
        self.assertIsInstance(self.city.name, str)
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def name_setter(self):
        self.city.name = "Kigali"
        set.asserEqual(self.city.name, "Kigali")

    def name_getter(self):
        self.city.name = "Gisenyi"
        self.assertEqual(self.city.name, "Gisenyi")

    def city_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_erros, 0, "PEP8 errors found")

    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

if __name__ == "__main__":
    unittest.main()
