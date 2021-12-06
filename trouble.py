#!/usr/bin/env python3  
from sys import argv, stderr
from os import chdir
from os.path import realpath, dirname, join as join_path
from site import addsitedir

basedir = dirname(realpath(argv[0]))
addsitedir(basedir)

from Board import Board
from AI import UserAI, FirstAI, LastAI

if __name__ == "__main__":
    uai = UserAI()
    fai = FirstAI()
    lai = LastAI()
    Gamers = (
        ("red","R",lai),
        ("blue","B",fai),
        ("yellow","Y",fai),
        ("green","G",lai),
    )
    for s in Board(Gamers,4,7).run():
        print("Player {:<9} finished after {:03d} turns, moved {:03d} times, and rolled again {:03d} times.".format(s[0],s[1],s[2],s[3]))