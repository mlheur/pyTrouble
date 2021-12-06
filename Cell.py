#!/usr/bin/env python3  
from sys import argv, stderr
from os import chdir
from os.path import realpath, dirname, join as join_path
from site import addsitedir

basedir = dirname(realpath(argv[0]))
addsitedir(basedir)

class Cell(object):

    def __init__(self,head,occupant=None) -> None:
        super().__init__()
        self.occupant = occupant
        if head is None:
            self.next = self
            self.last = self
        else:
            self.next = head
            self.last = head.last
            head.last = self
        self.exit_id = None

    def is_occupied(self):
        return self.occupant is not None

    def clear(self):
        token = self.occupant
        self.occupant = None
        return token

    def occupy(self,token):
        if self.is_occupied():
            return self.occupant
        self.occupant = token
        return None
    
    def set_exit(self,player):
        self.exit_id = player.id
        self.exit = player.base

    def seek_ahead(self,player,amount):
        ahead = self
        while amount > 0:
            amount -= 1
            ahead = ahead.get_next(player)
            if ahead is None: return ahead
        return ahead
    
    def get_next(self,player):
        if self.exit_id == player.id:
            return self.exit
        return self.next
    
    def __str__(self) -> str:
        if self.is_occupied(): return str(self.occupant)
        return "__"