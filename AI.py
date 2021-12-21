#!/usr/bin/env python3  
from sys import argv, stderr
from os import chdir, terminal_size
from os.path import realpath, dirname, join as join_path
from site import addsitedir

basedir = dirname(realpath(argv[0]))
addsitedir(basedir)

class TroubleAI(object):
    AI = "UNDEF"
    def choose(self,player,options):
        pass
    def __str__(self) -> str:
        return self.AI


class UserAI(TroubleAI):
    AI = "USER"
    def choose(self,player,options):
        choice_str = ""
        while len(choice_str) == 0:
            print("{}".format(player.board))
            choice_str = input("Choose wisely, {}! ".format(player.name))

        try:
            choice = int(choice_str)
        except ValueError as ve:
            choice = 0
        
        if choice == 0 or choice > len(options): choice = None
        else: choice = options[choice-1]
        
        return choice

class FirstAI(TroubleAI):
    AI = "FIRST"
    def choose(self,player,options):
        return options[0]

class LastAI(TroubleAI):
    AI = "LAST"
    def choose(self,player,options):
        return options[len(options)-1]

class AheadAI(TroubleAI):
    AI = "AHEAD"
    def choose(self,player,options):
        best_choice = None
        least_distance = 0
        for opt in options:
            (token,dest) = opt
            distance = token.distance_to_base()
            if distance < least_distance or least_distance == 0:
                best_choice = opt
                least_distance = distance
        return best_choice

class BehindAI(TroubleAI):
    AI = "BEHIND"
    def choose(self,player,options):
        best_choice = None
        most_distance = 0
        for opt in options:
            (token,dest) = opt
            distance = token.distance_to_base()
            if distance > most_distance or most_distance == 0:
                best_choice = opt
                most_distance = distance
        return best_choice


class AttackAI(AheadAI):
    AI = "ATTACK"
    def choose(self,player,options):
        best_choice = None
        most_distance = 0
        for opt in options:
            (token,dest) = opt
            if dest.is_occupied():
                return opt
        return super().choose(player,options)
