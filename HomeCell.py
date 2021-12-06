#!/usr/bin/env python3  
from sys import argv, stderr
from os import chdir
from os.path import realpath, dirname, join as join_path
from site import addsitedir

basedir = dirname(realpath(argv[0]))
addsitedir(basedir)
from Cell import Cell

class HomeCell(Cell):
    def __init__(self, player, head, occupant) -> None:
        super().__init__(head, occupant)
        self.player = player
        self.exit_id = player.id
        self.exit = player.start
    
    def seek_ahead(self, player, amount, for_display = False):
        if not for_display: return super().seek_ahead(self,player,amount)
        ahead = self
        while amount > 0:
            amount -= 1
            ahead = ahead.next
            if ahead is None: return ahead
        return ahead

    def __str__(self) -> str:
        #return "{:02d}".format(self.id)
        if self.is_occupied(): return str(self.occupant)
        return "{}H".format(self.player)