#!/usr/bin/env python3  
from sys import argv, stderr
from os import chdir
from os.path import realpath, dirname, join as join_path
from site import addsitedir

basedir = dirname(realpath(argv[0]))
addsitedir(basedir)
from Token import DummyToken as Token

class Cell(object):

    next_id = 0

    def __init__(self,head) -> None:
        super().__init__()
        self.id = Cell.next_id
        Cell.next_id += 1
        self.exit_id = None
        self.type = 0
        self.occupant = None
        if head is None:
            self.next = self
            self.last = self
        else:
            head.last.next = self
            self.next = head
            self.last = head.last
            head.last = self


    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id

    def is_occupied(self):
        return self.occupant is not None

    def clear(self):
        token = self.occupant
        self.occupant = None
        return token

    def occupy(self,token):
        if self.occupant is not None:
            self.occupant.boot()
        if token.location is not None:
            token.location.occupant = None
        token.location = self
        self.occupant = token
    
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
    
    def distance_to_base(self,player):
        i = self
        n = 0
        while i is not None and i.type < 1:
            n += 1
            i = i.get_next(player)
        return n
    
    def get_next(self,player):
        if self.exit_id == player.id:
            return self.exit
        return self.next
    
    def __str__(self) -> str:
        #return "{:02d}".format(self.id)
        if self.is_occupied(): return str(self.occupant)
        return "__"
