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
        self.player = player
        self.id     = id
        print ("Created Token p:{} id:{}".format(player,id))
    def __str__(self) -> str:
        return "{}{}".format(self.player,self.id)


