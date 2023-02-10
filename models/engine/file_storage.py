#!/usr/bin/python3
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity


class FileStorage():
    __file_path = "file.json"
    __object = {}

    def do_all(self):
        return self.__objects
    def do_new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def do_save(self):
        new_dict = {}
        for a, b in self.__objects.items():
            new_dict[a] = b.dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        new_obj_dict = {}
        try:
            with open(self.__file_path, mode="r", encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
                for a, c in new_obj_dict.items():
                    self.__object[k] = eval(c["__class__"](**c)
        except FileNotFoundError:
            pass
