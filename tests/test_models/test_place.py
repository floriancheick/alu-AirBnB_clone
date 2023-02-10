#!/usr/bin/python3

import models
import unittest
import pep8
from datetime import datetime
from models.place import Place

class TestPlace(unittest.TestCase):
    def set_up(self):
        self.place = Place()

    def city_id(self):
        self.assertIsInstance(self.place.city_id, str)
        self.assertEqual(self.place.city_id, "")

    def user_id(self):
        self.assertIsInstance(self.place.user_id, str)
        self.asserEqual(self.place.user_id, "")

    def do_name(self):
        self.assertIsInsatnce(self.place.name, str)
        self.assertEqual(self.place.name, "")

    def description(self):
        self.assertIsInstance(self.place.description, str)
        self.assertEqual(self.place.description, "")

    def number_rooms(self):
        self.asssertIsInstance(self.place.number_bathrooms, int)
        self.assertEqual(self.palce.number_bathrooms, 0)

    def number_bathrooms(self):
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertEqual(self.place.number_bathrooms, 0)
    def max_guest(self):
        self.asssertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.max_guest, 0)

    def night_price(self):
        self.assertIsInsatnce(self.place.night_price, int)
        self.asserEqual(self.place.night_price, 0)
    def latitude(self):
        self.assertIsInstance(self.place.latitude, float)
        self.assertEqual(self.place.latitude, 0.0)

    def longitude(self):
        self.assertIsInstance(self.place.longitude, float)
        self.assertEqual(self.palce.longitude, 0.0)

    def amenity_id(self):
        self.assertIsInstance(self.place.amenity_id, list)
        self.assertEqual(self.place.amenity_id, [])

    def Place_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep*style.check_files(['mdels/palce.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 erros found")

if __name__ == "__main__"
    unittest.main()
