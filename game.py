##################################################
# RansackIt
#
# Written by Jacob Adams 
##################################################



##################################################
# Module imports
##################################################

import tkinter as tk
import random
import math

import unit
import rescource
import player
import dice
import map



##################################################
# Main game class
##################################################
class Game:
    def __init__(
            self, 
            master,
            players=[player.Player(0, "Player 1"), player.Player(1, "Player 2")]
            ):
        
        self.master = master
        self.canvas = tk.Canvas(self.master, bg="black", width=1000, height=8000)

        self.players = players
        self.player_turn = 0
        self.round = 0


        self.map = map.Map(20, 10, self)

    def draw(self):
        self.canvas.delete("all")
        self.map.draw()

        return self.canvas
    

    def add_rescources(self, number):

        for p in self.players:
            pass
