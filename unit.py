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

import player

def draw_unit(canvas, x, y, colour, text):
    canvas.create_rectangle(x, y, x+16, y+16, fill=colour)
    canvas.create_text(x+8, y+8, text=text, fill="white", font=("Arial",8))

class Unit:
    def __init__(self, owner_ID):
        self.owner_ID = owner_ID
        self.unit_colour = player.PLAYER_COLOURS[owner_ID]

    def draw(self, canvas, x, y):
        draw_unit(canvas, x, y, self.unit_colour, "NA")

    def get_dice(self):
        return 0
    
    def can_work_tiles(self):
        return False
    
    def can_build(self):
        return False
    
    def get_movement(self):
        return {"WALK" : 1, "SWIM" : 2, "FLY" : 0}

class Worker(Unit):
    def __init__(self, owner_ID):
        super().__init__(owner_ID)

    def draw(self, canvas, x, y):
        draw_unit(canvas, x, y, self.unit_colour, "B")

    def get_dice(self):
        return 1
    
    def can_work_tiles(self):
        return True
    
    def can_build(self):
        return True
    
    def get_movement(self):
        return {"WALK" : 1, "SWIM" : 2, "FLY" : 0}

class Warrior(Unit):
    def __init__(self, owner_ID):
        super().__init__(owner_ID)

    def draw(self, canvas, x, y):
        draw_unit(canvas, x, y, self.unit_colour, "W")

    def get_dice(self):
        return 4
    
    def can_work_tiles(self):
        return False
    
    def can_build(self):
        return False
    
    def get_movement(self):
        return {"WALK" : 1, "SWIM" : 2, "FLY" : 0}

class Knight(Unit):
    def __init__(self, owner_ID):
        super().__init__(owner_ID)

    def draw(self, canvas, x, y):
        draw_unit(canvas, x, y, self.unit_colour, "K")

    def get_dice(self):
        return 8
    
    def can_work_tiles(self):
        return False
    
    def can_build(self):
        return False
    
    def get_movement(self):
        return {"WALK" : 1, "SWIM" : 2, "FLY" : 0}

class Cannon(Unit):
    def __init__(self, owner_ID):
        super().__init__(owner_ID)

    def draw(self, canvas, x, y):
        draw_unit(canvas, x, y, self.unit_colour, "C")

    def get_dice(self):
        return 12
    
    def can_work_tiles(self):
        return False
    
    def can_build(self):
        return False
    
    def get_movement(self):
        return {"WALK" : 1, "SWIM" : 2, "FLY" : 0}
    
class Dragon(Unit):
    def __init__(self, owner_ID):
        super().__init__(owner_ID)

    def draw(self, canvas, x, y):
        draw_unit(canvas, x, y, self.unit_colour, "D")

    def get_dice(self):
        return 20
    
    def can_work_tiles(self):
        return False
    
    def can_build(self):
        return False
    
    def get_movement(self):
        return {"WALK" : 0, "SWIM" : 0, "FLY" : 2}