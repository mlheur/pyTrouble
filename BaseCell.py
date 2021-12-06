#!/usr/bin/env python3  
from sys import argv, stderr
from os import chdir
from os.path import realpath, dirname, join as join_path
from site import addsitedir

basedir = dirname(realpath(argv[0]))
addsitedir(basedir)
from Cell import Cell

class BaseCell(Cell):
    def __init__(self, player, head) -> None:
        super().__init__(head, None)
        self.player = player
    def __str__(self) -> str:
        if self.is_occupied(): return str(self.occupant)
        return "{}B".format(self.player)