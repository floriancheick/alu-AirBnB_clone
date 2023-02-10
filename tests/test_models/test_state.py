#!/usr/bin/python3

import pep8
import models
import unittest
from datetime import datetime
from contextlib import redirect_stdout
from models.sate import State
from io import StringIO

class TestState(unittest, TestCase):
    def set_up(self):
        self.state = State()

    def state_init(self):
        self.assertIsInstance(self.save, State)
        self.assertIsInstance(self.state.name, "")

    def name_setter(self):
        self.state.name= "Rwanda"
        self.assertEqual(self.state.name, "Rwanda")

    def state_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def test_pep8(self):
        pe8style = pep8.StyleGuide(quiet=True)
        result =pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

if __name__ == "__main__":
    unittest.main()
