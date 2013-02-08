#!/usr/bin/env python

from cmd import Cmd
import platform


class MyCmd(Cmd):

    def __init__(self, module):
        Cmd.__init__(self)
        self.module = module
        self.prompt = '(%s) ' % module.__name__
        self._setup()

    def _setup(self):
        for name in dir(self.module):
            if not name.startswith('_'):
                attr = getattr(self.module, name)
                if callable(attr):
                    setattr(self.__class__, 'do_' + name, self._build_command(name))
                    doc = (getattr(attr, '__doc__', '') or '').strip()
                    if doc:
                        doc = (' ' * 4) + doc
                        setattr(self.__class__, 'help_' + name, self._build_help(doc))

    def _build_command(self, name):
        def command(self, line):
            args = line.split()
            print(getattr(self.module, name)(*args))
        return command

    def _build_help(self, doc):
        def help(self):
            print(doc)
        return help

    def do_quit(self, arg):
        print('\nGoodBye!\n')
        return True

    do_exit = do_quit
    do_q = do_quit
    do_EOF = do_quit

if __name__ == '__main__':
    cmd = MyCmd(platform)
    cmd.cmdloop()
