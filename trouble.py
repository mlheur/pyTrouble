#!/usr/bin/env python3  
from sys import argv, stderr
from os import chdir
from os.path import realpath, dirname, join as join_path
from site import addsitedir

basedir = dirname(realpath(argv[0]))
addsitedir(basedir)

from Board import Board
from AI import UserAI, FirstAI, LastAI, AheadAI, BehindAI

if __name__ == "__main__":
    uai = UserAI()
    aai = AheadAI()
    bai = BehindAI()
    fai = FirstAI()
    lai = LastAI()
    Gamers = (
        ("red","R",bai),
        ("blue","B",aai),
        ("yellow","Y",aai),
        ("green","G",aai),
    )

    stats = {
        'red':     {'avg': 0, 'qty': 0, 'ai': None},
        'blue':    {'avg': 0, 'qty': 0, 'ai': None},
        'yellow':  {'avg': 0, 'qty': 0, 'ai': None},
        'green':   {'avg': 0, 'qty': 0, 'ai': None}
    }

    def print_stats():
        print("")
        for color in stats.keys():
            print("{:<9} [{:<9}] {:.2f} after {} runs".format(color, stats[color]['ai'], stats[color]['avg'], stats[color]['qty']))

    def update_stat(color,ai,turns):
        stats[color]['ai'] = ai
        osum = stats[color]['avg'] * stats[color]['qty']
        nsum = osum + turns
        stats[color]['qty'] += 1
        stats[color]['avg'] = nsum / stats[color]['qty']

    for i in range(100000):
        b = Board(Gamers,4,7)
        b.run()
        #print("")
        for p in b.players:
            update_stat(p.name, p.ai.AI, p.turns)
            continue
            print("Player {:<9}, AI:{:<9} finished after {:3d} turns, moved {:3d} times, and rolled again {:2d} times.".format(
                p.name,
                p.ai.AI,
                p.turns,
                p.moves,
                p.rolled_again
            ))
        if i % 100 == 99: print_stats()
