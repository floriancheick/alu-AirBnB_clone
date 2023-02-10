#!/usr/bin/python3

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setup(self):
        self.base = BaseModel()
        self.store = FileStorage()

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def save_reload(self):
        self.base.name = "Max"
        self.base.my_number = 1
        name = str(self.base.__class__.__name__)
        key = f"{name}.{str(self.base.id)}"
        self.base.save()
        self.assertTrue(os.path.exists('filer.json'))
        self.store.reload()
        obj = self.store.all()
        self.assertIsNotNone(obj[key])
        self.obj_reload = obj[key]
        self.assertTrue(self.obj_reload, BaseModel)
        self.asserTrue(self.base is not self.obj_reload)
        self.assertTrue(self.base.created != self.base.updated)

class TestSave(unittest.TestCase):
    def base_model_save(self):
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))
