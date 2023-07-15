#!/usr/bin/python3
"""
   Module contains entry point to cmd interpreter
"""

import cmd
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Class for console """

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """ Quit cmd to exit program """
        return True

    def do_EOF(self, arg):
        """ end of file """
        return True

    def emptyline(self):
        """ emptyline """
        pass

    def do_create(self, line):
        """ creates new instance of Basemodel """
        arg_list = line.split()
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Review"]

        if not arg_list:
            print("** class name missing **")
        else:
            if arg_list[0] in classes:
                new_model = eval(arg_list[0] + "()")
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """ prints string rep of an instance """
        storage = FileStorage()
        arg_list = line.split()
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Review"]

        storage.reload()

        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            dicts = storage.all()
            instance = arg_list[0] + '.' + arg_list[1]
            if instance in dicts.keys():
                print(dicts[instance])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """ deletes an an instance and save changes to json file """
        storage = FileStorage()
        arg_list = line.split()
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Review"]

        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            instance = arg_list[0] + '.' + arg_list[1]
            if instance in objs.keys():
                del objs[instance]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """ prints string instance of all instances """
        storage = FileStorage()
        arg_list = line.split()
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Review"]

        if not arg_list or arg_list[0] not in classes:
            str_list = []
            objs = storage.all()
            for instance in objs.values():
                str_list.append(instance.__str__())
            print(str_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ updates an an instance and save changes to json file """
        storage = FileStorage()
        arg_list = line.split()
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Review"]

        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif len(arg_list) == 2:
            print("** attribute id missing **")
        elif len(arg_list) == 3:
            print("** value missing **")
        else:
            objs = storage.all()
            instance = arg_list[0] + '.' + arg_list[1]
            if instance in objs.keys():
                for value in objs.values():
                    try:
                        attr_type = type(getattr(value, arg_list[2]))
                        arg_list[3] = attr_type(arg_list[3])
                    except AttributeError:
                        pass
                setattr(value, arg_list[2], arg_list[3])
                storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
