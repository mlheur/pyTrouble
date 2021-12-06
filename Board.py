#!/usr/bin/env python3  
from sys import argv, stderr
from os import chdir
from os.path import realpath, dirname, join as join_path
from site import addsitedir
from random import randint

basedir = dirname(realpath(argv[0]))
addsitedir(basedir)

from Cell import Cell
from Player import Player

class Board(object):

    def __init__(self,colors,C,token_qty,cells_per_player) -> None:
        super().__init__()
        self.colors           = colors
        self.C                = C
        self.players          = list()
        self.head             = Cell(None)
        self.cells_per_player = cells_per_player
        self.token_qty        = token_qty
        for p in range(len(colors)):
            self.players.append(Player(self,p))
        
        for p in self.players: p.start.last.set_exit(p)
    
    def roll(self):
        return randint(1,6)

    def redraw(self):
        print(str(self))

    def run(self):
        print(str(self))
        players_are_active = True
        while(players_are_active):
            players_are_active = False
            for p in self.players:
                if not p.is_finished():
                    players_are_active = True
                    p.move()

    def __str__(self) -> str:
        board_str = ""

        # print Home cells
        for line_no in range(self.token_qty):
            line = "HOME_{:02d}  ".format(line_no)
            for p in self.players:
                line = "{}{} ".format(line,p.home.seek_ahead(p,line_no,True))
            board_str = "{}{}\n".format(board_str,line)

        # print Game cells
        for line_no in range(self.cells_per_player):
            line = "GAME_{:02d}  ".format(line_no)
            for p in self.players:
                line = "{}{} ".format(line,p.start.seek_ahead(p,line_no))
            board_str = "{}{}\n".format(board_str,line)

        # print Base cells
        for line_no in range(self.token_qty):
            line = "BASE_{:02d}  ".format(line_no)
            for p in self.players:
                line = "{}{} ".format(line,p.base.seek_ahead(p,line_no))
            board_str = "{}{}\n".format(board_str,line)

        return board_str


