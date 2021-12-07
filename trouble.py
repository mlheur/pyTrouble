#!/usr/bin/env python3  
from sys import argv, stderr
from os import chdir, stat
from os.path import realpath, dirname, join as join_path
from site import addsitedir

basedir = dirname(realpath(argv[0]))
addsitedir(basedir)

from Board import Board
from AI import UserAI, FirstAI, LastAI, AheadAI, BehindAI, AttackAI
from Stats import Stats

if __name__ == "__main__":
    uai = UserAI()
    aaai = AttackAI()
    aai = AheadAI()
    bai = BehindAI()
    fai = FirstAI()
    lai = LastAI()
    gamers = (
        ("red","R",aaai),
        ("blue","B",aaai),
        ("yellow","Y",bai),
        ("green","G",aai),
    )

    stats = Stats(gamers)

    for i in range(100000):
        b = Board(gamers,4,7)
        b.run()
        for p in b.players:
            stats.update(p)
            continue
        if i % 1000 == 999: stats.show(b)
