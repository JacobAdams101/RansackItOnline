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
import building



##################################################
# Main game class
##################################################
class Game:
    def __init__(
            self, 
            master,
            players=[player.Player(0, "Player 1"), player.Player(1, "Player 2")]
            ):
        
        self.width = 1000
        self.height = 700

        self.master = master
        self.canvas = tk.Canvas(self.master, bg="black", width=self.width, height=self.height)

        self.players = players
        self.player_turn = 0
        self.round = 0

        #Create the map
        self.map = map.Map(20, 10, self.canvas, self.on_hex_click, self.on_unit_click)

        self.selected = None

    def is_founding_turn(self):
        return self.round == 0
    
    def get_player_turn(self):
        return self.players[self.player_turn]
    

    def draw_selected(self, canvas, x_origin, y_origin, box_width=128, box_height = 64):
        canvas.create_rectangle(x_origin, y_origin, x_origin+box_width, y_origin+box_height, fill="#a0a0a0")
        canvas.create_text(x_origin+(box_width//2), y_origin+(box_height//2)-6, text="Selected", fill="black", font=("Arial",12))
        message = None
        if self.selected is not None:
            if isinstance(self.selected, unit.Unit):
                message = f"Unit {type(self.selected).__name__}"
            elif isinstance(self.selected, map.Hex):
                message = f"Hex {type(self.selected).__name__}"
        canvas.create_text(x_origin+(box_width//2), y_origin+(box_height//2)+6, text=message, fill="black", font=("Arial",12)) 
    
    def draw(self):
        self.canvas.delete("all")
        self.map.draw()

        if self.is_founding_turn():
            self.players[self.player_turn].draw(self.canvas, 0, self.height-100, message="Found your city")

            self.players[self.player_turn].inventory.draw(self.canvas, 138, self.height-100)

            self.draw_selected(self.canvas, self.width-200, self.height-100, box_width=128, box_height = 64)
        else:
            self.players[self.player_turn].draw(self.canvas, 0, self.height-100, message="It's your turn!")

            self.players[self.player_turn].inventory.draw(self.canvas, 138, self.height-100)

            self.draw_selected(self.canvas, self.width-200, self.height-100, box_width=128, box_height = 64)

        return self.canvas
    
    def num_players(self):
        return len(self.players)
    
    def next_turn(self):
        self.player_turn += 1
        if self.player_turn == self.num_players():
            self.player_turn = 0
            self.round += 1

        self.run_turn()

        self.selected = None

    #An alias for run turn to make it more obvious this is how the game starts
    def start_game(self):
        self.run_turn()
    
    """
    Run a player's turn
    """
    def run_turn(self):
        p = self.players[self.player_turn]
        if self.is_founding_turn():
            pass
        else: 
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

        #Draw updates
        self.draw()
    

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

        tax = (pop+1)//2
        print(f"ADDING TAX {tax} (population {pop})")
        #Tax = pop /2
        p.inventory.add([rescource.Rescource(rescource.RESCOURCE_COIN, tax)])

    def add_rescources(self, number):
        #Loop through all players
        for p in self.players:
            #Loop through map
            for x in range(self.map.width):
                for y in range(self.map.height):
                    #If the current hex has the correct rescource numbers
                    if self.map.world[x][y].rescource_number != number:
                        continue
                    #Figure out who gets rescources (and what)
                    pID, rescource_type = self.map.world[x][y].who_gets_rescources()
                    if pID is None: #If no one gets rescource
                        continue
                    #If this hex is owned by the current player
                    if pID == p.ID:
                        #Add rescources
                        p.inventory.add(self.map.world[x][y].get_rescources(rescource_type))


    def on_hex_click(self, e, q, r, hex_tile):
        print(f"Hex clicked at ({q},{r}), type: {type(hex_tile).__name__}")
        if self.is_founding_turn():
            hex_tile.buildings.append(building.Village(self.get_player_turn().ID))
            self.next_turn()
        else:
            hex_tile.units.append(unit.Warrior(self.get_player_turn().ID))

        self.selected = hex_tile

        self.draw()

    def on_unit_click(self, e, q, r, hex_tile, unit):
        print(f"Hex clicked at ({q},{r}), hex type: {type(hex_tile).__name__}, unit type: {type(unit).__name__}")

        self.selected = unit
        
        self.draw()


