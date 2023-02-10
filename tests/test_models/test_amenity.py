#!/usr/bin/python3

import models
import pep8
import unittest
from io import StringIO
from datetime import datetime
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def set_up(self):
        self.amenit = Amenity()

    def amenity_init(self):
        self.assertIsInstance(self.amenity.name, str)
        self.asserIsInstance(self.amenity, Amenity)
        self.assertEqual(self.amenity.name, "")

    def name_setter(self):
        self.amenity.name = "Internet"
        self.asssertEqual(self.amenity.anme, "Internet")

    def name_getter(self):
        self.amenity.name = "Electricity"
        self.assertEqual(self.amenity.name, "Electricity")
    def amenity_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.asssertEqual(resutl.total_erros, 0, "PEP8 errors found")

    def pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.totoal_errors, 0, "PEP8 errors found")

if __name__ == "__main__"
    unittest.main()
