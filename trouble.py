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
    AISet = {
        "UserAI": UserAI(),
        "AttackAI": AttackAI(),
        "AheadAI": AheadAI(),
        "BehindAI": BehindAI(),
        "FirstAI": FirstAI(),
        "LastAI": LastAI()}

    AssignedAI = {}
    for n in range(4):
        if len(argv) > n+1: AssignedAI[n] = argv[n+1]
        else: AssignedAI[n] = "UserAI"

    gamers = (
        ("red","R",AISet[AssignedAI[0]]),
        ("blue","B",AISet[AssignedAI[1]]),
        ("yellow","Y",AISet[AssignedAI[2]]),
        ("green","G",AISet[AssignedAI[3]]),
    )

    stats = Stats(gamers)

    for i in range(100000):
        b = Board(gamers,4,7)
        try:
            b.run()
        except KeyboardInterrupt as ki:
            stats.show(b)
            break
        for p in b.players:
            stats.update(p)
        if i % 1000 == 999: stats.show(b)
