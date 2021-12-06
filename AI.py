#!/usr/bin/env python3  
from sys import argv, stderr
from os import chdir, terminal_size
from os.path import realpath, dirname, join as join_path
from site import addsitedir

basedir = dirname(realpath(argv[0]))
addsitedir(basedir)

class TroubleAI(object):
    def choose(self,player,targets):
        pass


class UserAI(TroubleAI):
    def choose(self,player,targets):
        choice_str = ""
        while len(choice_str) == 0:
            choice_str = input("Choose wisely! ")

        try:
            choice = int(choice_str)
        except ValueError as ve:
            choice = 0
        
        if choice == 0 or choice > len(targets): choice = None
        else: choice = targets[choice-1]
        
        return choice

class FirstAI(TroubleAI):
    def choose(self,player,targets):
        return targets[0]

class LastAI(TroubleAI):
    def choose(self,player,targets):
        return targets[len(targets)-1]

class AheadAI(TroubleAI):
    def choose(self,player,targets):
        return targets[len(targets)-1]