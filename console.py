#!/usr/bin/python3
""" Console Module """

import cmd
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.base_models import BaseModel
from models.engine.file_sorage import  FileStorage

class HBNBCommand(cmd.Cmd):
    """Command"""
    prompt = "(hbnb)"
    class_list = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def quit(self, line):
        """quit if the command is used"""
        return True

    def EOF(self, line):
        """Exit """
        print()
        return True

    def empty_line(self):
        pass

    def make(self, line):
        """new instance of BaseModel"""
        if not line:
            print("** class missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")
        else:
            maker = eval(line)()
            maker.save()
            print(maker.id)

    def view(self, line):
        line_list = line.split(" ")
        if not line:
            print("** class missinf **")
        elif line_list[0] not in self.class_list
            print("** class doesn't exist **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        else:
            tmp_dict = FileStorage().all()
            key = f"{line_list[0]}.{line_list[1]}"
            if key in tmp_dict:
                print(tmp_dict[key])
            else:
                print("** no instance found **")

    def del(self, line):
        """deletes an instance based on the class name and id"""
        line_list = line.split(" ")
        if not line:
            print("** class missing **")
        elif line_list[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        else:
            tmp_dict = FileStorage().all()
            key = f"{line_list[0]}.{line_list[1]}"
            if key in tmp_dict:
                del tmp_dict[key]
                FileStorage().save()
            else:
                print("** no instance found **")

    def all(self, line):
        line = line.split(" ")
        obj_list = []
        tmp_dict = FileStorage().all()
        if len(line) == 0:
            for obj in tmp_dict.values():
                obj_list.append(str(obj))
            print(obj_list)
        elif line[0] in self.class_list:
            for key, val in tmp_dict.items():
                if line_list[0] in key:
                    obj_list.append(str(val))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def update(self, line):
        line_list = line.split(" ")
        if not line:
            print("** class missing **")
        elif line_list[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            tmp_dict = FileStorage().all()
            key = f"{line_list[0]}.{line_list[1]}"
            if key not in tmp_dict:
                print("** no instance found **")
            elif len(line_list) == 2:
                print("** attribute missing **")
            elif len(line_lsit) == 3:
                print("** value missing **")
            else:
                casting = type(eval(line_list[3]))
                arg_3 = line_list[3]
                arg_3 = arg_3.strip("'")
                arg_3 = arg_3.strip('"')
                setattr(tmp_dict.get(key), line_list[2], casting(arg_3))
                tmp_dict[key].save()

if __name__ == '__main__'
    HBNBCommand().cmdloop()  
