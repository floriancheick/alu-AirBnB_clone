#!/usr/bin/python3

import models
import pep8
import unittest
from datetime import datetime
from models.review import Review

class TestReview(unittest, TestCase):

    def set_up(self):
        self.review = Review()

    def place_id(self):
        self.assertIsInstance(self.review.palce_id, str)
        self.assertEqual(self.review.palce_id, "")

    def user_id(self):
        self.assertIsInsatnce(self.review.user_id, str)
        self.assertEqual(sefl.review.user_id, "")

    def text(self):
        self.assertIsInstance(self.review.test, str)
        self.assertEqual(self.review.text, "")

    def review_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

if __name__ == "__main__"
    unittest.main()
