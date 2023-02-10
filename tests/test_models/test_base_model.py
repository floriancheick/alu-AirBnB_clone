#!/usr/bin/python3
"""
module
"""

import unittest
from io import StringIO
from datetime import datetime
from contextlib import redirect_stdout
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def to_dict(self):
        copy = BaseModel()
        copy_dict = copy.to_dict()
        self.assertIsInstance(copy_dict["created_at"], str)

    def unique_id(self):
        copy = BaseModel()
        copy_2 = BaseModel()
        self.assertNotEqual(copy.id, copy_2.id)
    def created_at(self):
        copy = BaseModel()
        self.assertIsInstance(copy.created_at, datetime)

    def str(self):
        with StringIO() as bufr, redirect_stdout(bufr):
            my_cop = BaseModel()
            print(my_cop.__str__())
            a = bufr.getvalue()
        self.assertIn(f"[{my_cop.__class__.__name__}] ({my_cop.id}) {my_cop.__dict__}",a)

    def save(self):
        copy_1 = BaseModel()
        copy_1.name = "James"
        copy_1.save()
        self.assertNotEqual(copy_1.created_at, copy_1.update_at)

    if __name__ == "__main__":
        unittest.main()
