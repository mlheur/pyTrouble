#!/usr/bin/env python3  
from sys import argv, stderr
from os import chdir
from os.path import realpath, dirname, join as join_path
from site import addsitedir

basedir = dirname(realpath(argv[0]))
addsitedir(basedir)

from Cell import Cell
from Token import Token
from HomeCell import HomeCell
from BaseCell import BaseCell

class Player(object):

    def __init__(self,board,id) -> None:
        super().__init__()
        self.board = board
        self.id = id
        if id == 0:
            self.start = board.head
        else:
            self.start = Cell(board.head)

        self.home = HomeCell(self,None,Token(self,0))
        self.base = BaseCell(self,None)
        for t in range(1,board.token_qty):
            self.last_home = HomeCell(self,self.home,Token(self,t))
            self.last_base = BaseCell(self,self.base)
        self.last_base.next = None

        for c in range(1,board.cells_per_player):
            Cell(board.head)
    
    def __str__(self) -> str:
        return self.board.C[self.id]