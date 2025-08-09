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

        #Create the map
        self.map = map.Map(20, 10, self)

    def draw(self):
        self.canvas.delete("all")
        self.map.draw()

        return self.canvas
    
    """
    Run a player's turn
    """
    def run_turn(self, p):
        #Taxes
        self.add_taxes(p)

        #Resources
        #Roll dice
        dice_1 = dice.roll_dice(6)
        dice_2 = dice.roll_dice(6)
        dice_roll = dice_1 + dice_2

        if dice_roll == 7: #Bandit/Pirate
            pass
        else: #Normal play
            self.add_rescources(dice_roll)
    

    def get_population(self, p):
        population = 0
        #Loop through map
        for x in range(self.map.width):
            for y in range(self.map.height):
                if len(self.map.world[x][y].buildings) > 0 and self.map.world[x][y].buildings[0].owner_ID == p.ID:
                    for b in self.map.world[x][y].buildings:
                        population += b.get_pop()
        
        #Return population
        return population

    def add_taxes(self, p):
        pop = self.get_population(p)
        #Tax = pop /2
        p.inventory.add([rescource.Rescource(rescource.RESCOURCE_COIN, (pop+1)//2)])

    def add_rescources(self, number):
        #Loop through all players
        for p in self.players:
            #Loop through map
            for x in range(self.map.width):
                for y in range(self.map.height):
                    #If the current hex has the correct rescource numbers
                    if self.map.world[x][y].rescource_number == number:
                        #Figure out who gets rescources (and what)
                        pID, rescource_type = self.map.world[x][y].who_gets_rescources()
                        #If this hex is owned by the current player
                        if pID == p.ID:
                            #Add rescources
                            p.inventory.add(self.map.world[x][y].get_rescources(rescource_type))

