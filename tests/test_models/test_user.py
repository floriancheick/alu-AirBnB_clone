#!/user/bin/python3

import models
import unittest
import pep8
from io import StringIO
from models.user import User
from contextlib import redirect_stdout
from datetime import datetime

class TestUser(unittest.TestCase):
    def set_up(self):
        self.user = User()

    def email(self):
        self.assertIsInstance(self.user.email, str)
        self.assertEqual(self.user.email, "")

    def password(self):
        self.assertIsInstance(self.user.password, str)
        self.assertEqual(self.user.password, "")

    def first_name(self):
        self.assertIsInstance(self.user.first_name, str)
        self.assertEqual(self.user.first_name, "")

    def last_name(self):
        self.assertIsInstance(self.user.last_name, str)
        self.asssertEqual(self.user.last_name, "")

    def user_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

if __name__ == "__main__":
    unittest.main()
