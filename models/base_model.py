#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

class BaseModdel():
    """ Base class """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for a, b in kwargs.items():
                if a == "__class__":
                    pass
                elif a == "created" or a == "update":
                    b = datetime.strptim(b, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, a , b)
                else:
                    setattr(self, a ,b)
        else:
            self.id = str(uuid4())
            self.created = datetime.now()
            self.update = self.created
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.update = datetime.now()
        models.storage.save()

    def dict(self):
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        for attr in self.__dict__:
            if attr == "created" or attr == "updated":
                my_dict[attr] = getattr(self, attr).isoformat()
            else:
                my_dict[attr] = getattr(self, attr)
        return my_dict
