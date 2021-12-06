#!/usr/bin/env python3  
from sys import argv, stderr
from os import chdir, terminal_size
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
        self.tokens = list()
        if id == 0:
            self.start = board.head
        else:
            self.start = Cell(board.head)

        for t in range(self.board.token_qty):
            self.tokens.append(Token(self,t))

        self.home = HomeCell(self,None,self.tokens[0])
        self.base = BaseCell(self,None)
        for t in range(1,board.token_qty):
            self.last_home = HomeCell(self,self.home,self.tokens[t])
            self.last_base = BaseCell(self,self.base)
        self.last_base.next = None

        for c in range(1,board.cells_per_player):
            Cell(board.head)
    
    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id
    
    def move(self):
        die = self.board.roll()
        print("Player {} rolled a {}.".format(self.board.colors[self.id],die))

        move_options = list()

        for t in self.tokens:
            # home cell tokens can only move on 1 or 6.
            if t.location.type < 0 and die > 1 and die < 6: continue
            # get the target cell
            dest = t.location.seek_ahead(self,die)
            # make sure the roll doesn't exceed the available cells
            if dest is None: continue
            # make sure we're not already occupying the destination
            if dest.is_occupied() and dest.occupant.player == self: continue
            # then it's a valid move.
            move_options.append((t,dest))

        choice = self.choose(move_options)
        if choice is not None:
            choice[1].occupy(choice[0])
            self.board.redraw()

        # roll a 6, go again.
        if die == 6:
            return self.move()
        
        
    def choose(self,targets):
        print("Valid Moves:")
        if len(targets) == 0:
            print (" - None")
            return None
        for t in targets:
            print(" - {} targets {}".format(t[0],t[1]))
        
        choice_str = ""
        while len(choice_str) == 0:
            choice_str = input("Choose wisely! ")

        try:
            choice = int(choice_str)
        except ValueError as ve:
            choice = 0
        if choice == 0 or choice > len(self.tokens): choice = None
        else: choice = targets[choice-1]
        print("You chose [{}]".format(choice[0]))
        return choice

    def is_finished(self):
        B = self.base
        while(B is not None):
            if not B.is_occupied(): return False
            B = B.next
        return True
    
    def __str__(self) -> str:
        return self.board.C[self.id]