#!/usr/bin/env python3  
from sys import argv, stderr
from os import chdir
from os.path import realpath, dirname, join as join_path
from site import addsitedir

basedir = dirname(realpath(argv[0]))
addsitedir(basedir)

class Stats(object):
    def __init__(self, gamers) -> None:
        super().__init__()
        self.tracker = self.init(gamers)
    
    def init(self,gamers):
        tracker = dict()
        for g in gamers:
            tracker[g[0]] = {'avg': 0, 'qty': 0}
        return tracker

    def show(self,board):
        print("")
        for player in board.players:
            stat = self.tracker[player.name]
            print("{:<9} [{:<9}] {:.2f} after {} runs".format(
                player.name,
                str(player.ai),
                stat['avg'],
                stat['qty']))

    def update(self,player):
        stat = self.tracker[player.name]
        osum = stat['avg'] * stat['qty']
        nsum = osum + player.turns
        stat['qty'] += 1
        stat['avg'] = nsum / stat['qty']

