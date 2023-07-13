#!/usr/bin/python3
"""
   Module contains entry point to cmd interpreter
"""

import cmd

class  HBNBCommand(cmd.Cmd):
    """ Class for console """

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """ Quit cmd to exit program """
        return True

    def emptyline(self, arg):
        """ empty line """
        pass

    def do_EOF(self, arg):
        """ end of file """
        return True

if __name__ = "__main__":
    HBNBCommand().cmdloop()
