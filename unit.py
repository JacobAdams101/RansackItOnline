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

def draw_unit(canvas, x, y, colour, text):
    canvas.create_rectangle(x, y, x+16, y+16, fill=colour)
    canvas.create_text(x+8, y+8, text=text, fill="white", font=("Arial",8))

class Unit:
    def __init__(self):
        self.unit_colour = "#ff0000"

    def draw(self, canvas, x, y):
        draw_unit(canvas, x, y, self.unit_colour, "NA")

class Worker(Unit):
    def __init__(self):
        super.__init__()

    def draw(self, canvas, x, y):
        draw_unit(canvas, x, y, self.unit_colour, "B")

class Warrior(Unit):
    def __init__(self):
        super.__init__()

    def draw(self, canvas, x, y):
        draw_unit(canvas, x, y, self.unit_colour, "W")

class Knight(Unit):
    def __init__(self):
        super.__init__()

    def draw(self, canvas, x, y):
        draw_unit(canvas, x, y, self.unit_colour, "K")

class Cannon(Unit):
    def __init__(self):
        super.__init__()

    def draw(self, canvas, x, y):
        draw_unit(canvas, x, y, self.unit_colour, "C")