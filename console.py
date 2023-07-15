#!/usr/bin/python3
"""
   Module contains entry point to cmd interpreter
"""

import cmd
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Class for console """

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """ Quit cmd to exit program """
        return True

    def do_EOF(self, arg):
        """ end of file """
        return True

    def do_create(self, line):
        """ creates new instance of Basemodel """
        arg_list = line.split()
        classes = ["BaseModel"]

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
        classes = ["BaseModel"]

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
        classes = ["BaseModel"]

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
