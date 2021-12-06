#!/usr/bin/env python3  
from sys import argv, stderr
from os import chdir
from os.path import realpath, dirname, join as join_path
from site import addsitedir

basedir = dirname(realpath(argv[0]))
addsitedir(basedir)

from Board import Board

if __name__ == "__main__":
    colors = ("red","green","yellow","blue")
    C      = ("R",  "G",    "Y",     "B")
    Board(colors,C,4,7).run()
