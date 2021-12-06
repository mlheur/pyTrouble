#!/usr/bin/env python3  
from sys import argv, stderr
from os import chdir
from os.path import realpath, dirname, join as join_path
from site import addsitedir

basedir = dirname(realpath(argv[0]))
addsitedir(basedir)

class Token(object):
    def __init__(self,player,id) -> None:
        super().__init__()
        self.player   = player
        self.id       = id
        self.location = None
    
    def boot(self):
        # maybe there should be some error checking, but
        # if I did everything right, this will never go wrong :-o
        h = self.player.home
        while h is not None and h.type < 0:
            if not h.is_occupied():
                h.occupy(self)
                return
            h = h.next

    def __str__(self) -> str:
        return "{}{}".format(self.player,self.id+1)

class DummyToken(Token):
    def __init__(self): pass
    def boot(self): pass