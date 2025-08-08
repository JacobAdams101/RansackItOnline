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

OCEAN_HEX = "OCEAN"
PLAINS_HEX = "PLAINS"
FARM_HEX = "FARM"
HILLS_HEX = "HILLS"
MOUNTAIN_HEX = "HILLS"

# ---------- Utilities for hex grid ----------
HEX_SIZE = 32

def get_pixel_xy(q, r, hex_size):
    #Calculate hex dimensions
    hex_width = hex_size * 2
    hex_height = (3**0.5) * hex_size

     # Offset for staggered rows
    x_offset = q * (hex_width * 0.75)
    y_offset = r * hex_height + (q % 2) * (hex_height / 2)

    return x_offset+hex_size, y_offset+hex_size

def get_hex_points(q, r, hex_size=HEX_SIZE, facing=None, offset_x=0, offset_y=0):
    # Center position of hex
    x_center, y_center = get_pixel_xy(q, r, hex_size)

    x_center += offset_x
    y_center += offset_y

    # Calculate hex corner coordinates
    points = []
    for i in range(6):
        if facing is not None and (i == facing or (i+1)%6 == facing):
            continue
        angle = (60 * i - 30) * 3.14159 / 180
        x_i = x_center + hex_size * (math.sin(angle))
        y_i = y_center + hex_size * (math.cos(angle))
        points.extend([x_i, y_i])

    return points

def draw_hex_shadow(canvas, q, r, hex_size=HEX_SIZE):
    # Calculate hex corner coordinates
    points = get_hex_points(q, r)
    # Draw the hex
    canvas.create_polygon(points, outline="#202020", fill="#202020", width=2)

RESCOURCE_NUMBER_RADIUS = 8

def draw_hex(canvas, q, r, y_offset, fill_color, harbor, units, buildings, rescource_number=None, hex_size=HEX_SIZE):
    # Center position of hex
    x_center, y_center = get_pixel_xy(q, r, hex_size)
        
    y_center += y_offset

    # Calculate hex corner coordinates
    points = get_hex_points(q, r, offset_x=0, offset_y=y_offset)
    # Draw the hex
    hex_object = canvas.create_polygon(points, outline="black", fill=fill_color, width=2)
    if rescource_number is not None:
        # Draw the number token in center
        canvas.create_oval(
            x_center-RESCOURCE_NUMBER_RADIUS, 
            y_center-RESCOURCE_NUMBER_RADIUS, 
            x_center+RESCOURCE_NUMBER_RADIUS, 
            y_center+RESCOURCE_NUMBER_RADIUS, 
            fill="white"
            )
        canvas.create_text(x_center, y_center, text=str(rescource_number), fill="black")

    if harbor is not None:
        harbor.draw(canvas, q, r)

    for i, u in enumerate(units):
        u.draw(canvas, x_center + i*8, y_center)

    hex_select_object = canvas.create_oval(
            x_center-RESCOURCE_NUMBER_RADIUS-3, 
            y_center-RESCOURCE_NUMBER_RADIUS-3, 
            x_center+RESCOURCE_NUMBER_RADIUS+3, 
            y_center+RESCOURCE_NUMBER_RADIUS+3, 
            outline="red", 
            fill="", 
            width=4
            )
    
    canvas.itemconfigure(hex_select_object, state="hidden")


    return hex_object, hex_select_object

def draw_harbor(canvas, q, r, fill_color, facing, hex_size=HEX_SIZE):
    # Center position of hex
    x_center, y_center = get_pixel_xy(q, r, hex_size)

    # Calculate hex corner coordinates
    points = get_hex_points(q, r, facing=facing)

    # Draw the hex
    canvas.create_polygon(points, outline="black", fill=fill_color, width=2)

    canvas.create_oval(x_center-16, y_center-16, x_center+16, y_center+16, fill="white")
    canvas.create_text(x_center, y_center, text=str("3:1"), fill="black")

def draw_unit(canvas, x, y, text):
    canvas.create_rectangle(x, y, x+16, y+16, fill="white")
    canvas.create_text(x+8, y+8, text=text, fill="black", font=("Arial",8))

class Harbor:
    def __init__(self, facing):
        self.facing = facing

    def draw(self, canvas, q, r):
        draw_harbor(canvas, q, r, "#0000ff", self.facing)

class Hex:
    def __init__(
            self, 
            rescource_number, 
            can_units_walk, 
            can_units_swim, 
            can_units_fly,
            hex_colour,
        ):
        #Rescource numbers
        self.rescource_number = rescource_number
        #Units
        self.can_units_walk = can_units_walk
        self.can_units_swim = can_units_swim
        self.can_units_fly = can_units_fly
        #HEX visuals
        self.hex_colour = hex_colour

        self.harbor = None
        self.buildings = []
        self.units = []

        self.y_offset = -8

        self.hex_object = None
        self.hex_select_object = None

    def draw(self, canvas, q, r):
        return None
        

class OceanHex(Hex):
    def __init__(self, rescource_number):
        super().__init__(
            rescource_number=rescource_number,
            can_units_walk = False,
            can_units_swim = True,
            can_units_fly = True,

            hex_colour = "#7fb3ff"
            )
        
        self.y_offset = 0
        
    def draw(self, canvas, q, r):
        self.hex_object, self.hex_select_object = draw_hex(canvas, q, r, self.y_offset, self.hex_colour, self.harbor, self.units, self.buildings, rescource_number=None)
        
class DesertHex(Hex):
    def __init__(self, rescource_number):
        super().__init__(
            rescource_number=rescource_number,
            can_units_walk = True,
            can_units_swim = False,
            can_units_fly = True,

            hex_colour = "#e6d8a3"
            )
    
    def draw(self, canvas, q, r):
        self.hex_object, self.hex_select_object = draw_hex(canvas, q, r, self.y_offset, self.hex_colour, self.harbor, self.units, self.buildings, rescource_number=None)
        
class PlainsHex(Hex):
    def __init__(self, rescource_number):
        super().__init__(
            rescource_number=rescource_number,
            can_units_walk = True,
            can_units_swim = False,
            can_units_fly = True,

            hex_colour = "#a0cf7f"
            )
        
    def draw(self, canvas, q, r):
        self.hex_object, self.hex_select_object = draw_hex(canvas, q, r, self.y_offset, self.hex_colour, self.harbor, self.units, self.buildings, rescource_number=None)
        
class FarmHex(Hex):
    def __init__(self, rescource_number):
        super().__init__(
            rescource_number=rescource_number,
            can_units_walk = True,
            can_units_swim = False,
            can_units_fly = True,

            hex_colour = "#c2b280"
            )
        
    def draw(self, canvas, q, r):
        self.hex_object, self.hex_select_object = draw_hex(canvas, q, r, self.y_offset, self.hex_colour, self.harbor, self.units, self.buildings, rescource_number=self.rescource_number)
        
class ForestHex(Hex):
    def __init__(self, rescource_number):
        super().__init__(
            rescource_number=rescource_number,
            can_units_walk = True,
            can_units_swim = False,
            can_units_fly = True,

            hex_colour = "#228B22"
            )
        
    def draw(self, canvas, q, r):
        self.hex_object, self.hex_select_object = draw_hex(canvas, q, r, self.y_offset, self.hex_colour, self.harbor, self.units, self.buildings, rescource_number=self.rescource_number)
        
class HillsHex(Hex):
    def __init__(self, rescource_number):
        super().__init__(
            rescource_number=rescource_number,
            can_units_walk = True,
            can_units_swim = False,
            can_units_fly = True,

            hex_colour = "#c68642"
            )
        
    def draw(self, canvas, q, r):
        self.hex_object, self.hex_select_object = draw_hex(canvas, q, r, self.y_offset, self.hex_colour, self.harbor, self.units, self.buildings, rescource_number=self.rescource_number)

class MountainsHex(Hex):
    def __init__(self, rescource_number):
        super().__init__(
            rescource_number=rescource_number,
            can_units_walk = True,
            can_units_swim = False,
            can_units_fly = True,

            hex_colour = "#888888"
            )
        
    def draw(self, canvas, q, r):
        self.hex_object, self.hex_select_object = draw_hex(canvas, q, r, self.y_offset, self.hex_colour, self.harbor, self.units, self.buildings, rescource_number=self.rescource_number)

HEX_ORDER = [FarmHex, ForestHex, HillsHex, MountainsHex, OceanHex, PlainsHex, OceanHex, DesertHex, OceanHex, FarmHex, OceanHex, ForestHex, OceanHex, HillsHex, OceanHex, OceanHex, OceanHex]
NUMBER_ORDER = [6, 8, 5, 9, 4, 10, 3, 11, 2, 12, 5, 9]


class Map:
    def __init__(self, width, height):
        #Write dimensions
        self.width = width
        self.height = height

        #Get deck of cards
        hex_deck = []
        number_deck = []
        for i in range((width-2)*(height-2)):
            hex_deck.append(HEX_ORDER[i % len(HEX_ORDER)])
            number_deck.append(NUMBER_ORDER[i % len(NUMBER_ORDER)])


        
        harbor_deck = [Harbor for i in range((width+height)//2)]

        #Build grid
        self.world = [[None for y in range(height)] for x in range(width)]

        #Randomise hexes
        for x in range(width):
            for y in range(height):
                if x == 0 or x == width-1 or y == 0 or y == height-1:
                    self.world[x][y] = OceanHex(rescource_number=2)
                    continue
                index = random.randrange(0, len(hex_deck))
                index_2 = random.randrange(0, len(number_deck))
                self.world[x][y] = hex_deck[index](rescource_number=number_deck[index_2])

                del hex_deck[index]
                del number_deck[index_2]


        #Add harbors
        #Randomise the order the hexes are visited in
        coords = [(x, y) for x in range(width) for y in range(height)]
        random.shuffle(coords)
        #Iterate through randomised list
        for x, y in coords:
            if len(harbor_deck) == 0:
                break
            if type(self.world[x][y]) == OceanHex:
                y_step = (x+1)%2
                points = [(x-1, y+1-y_step), (x, y+1), (x+1, y+1-y_step), (x+1, y-y_step), (x, y-1), (x-1, y-y_step)]
                for i, (a, b) in enumerate(points):
                    if self.get_hex(a, b) is not None and type(self.get_hex(a, b)) != OceanHex:
                        index = random.randrange(0, len(harbor_deck))
                        
                        self.world[x][y].harbor = harbor_deck[index]((i+3)%6)

                        del harbor_deck[index]
                        break

    def get_hex(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.world[x][y]
        else:
            return None
    

    def on_hex_click(self, e, q, r, hex_tile):

        print(f"Hex clicked at ({q},{r}), type: {type(hex_tile).__name__}")

    def on_hex_enter(self, e, q, r, hex_tile):
        for q in range(len(self.world)):
            for r in range(len(self.world[q])):
                self.on_hex_leave(e, q, r, self.world[q][r])

        state = self.canvas.itemcget(hex_tile.hex_select_object, "state")
        if state == "hidden":
            self.canvas.itemconfigure(hex_tile.hex_select_object, state="normal")

    def on_hex_leave(self, e, q, r, hex_tile):
        state = self.canvas.itemcget(hex_tile.hex_select_object, "state")
        if state == "normal":
            self.canvas.itemconfigure(hex_tile.hex_select_object, state="hidden")   


    def draw_map(self, master):
        # Create a canvas to draw the map
        self.canvas = tk.Canvas(master, bg="black", width=1000, height=8000)

                

        # Loop through world grid and draw lower hexagons
        for q in range(len(self.world)):
            for r in range(len(self.world[q])):
                hex_tile = self.world[q][r]

                draw_hex_shadow(self.canvas, q, r)

                if hex_tile is None or hex_tile.y_offset != 0:
                    continue

                hex_tile.draw(self.canvas, q, r)

        # Loop through world grid and draw upper hexagons
        for q in range(len(self.world)):
            for r in range(len(self.world[q])):
                hex_tile = self.world[q][r]

                if hex_tile is None or hex_tile.y_offset == 0:
                    continue

                hex_tile.draw(self.canvas, q, r)


        for q in range(len(self.world)):
            for r in range(len(self.world[q])):
                hex_tile = self.world[q][r]

                self.canvas.tag_bind(
                    hex_tile.hex_object, 
                    "<Button-1>", 
                    lambda e, q=q, r=r, hex_tile=hex_tile: self.on_hex_click(e, q, r, hex_tile) #NOTE: lambda using optionals as otherwise broken
                    )
                
                self.canvas.tag_bind(
                    hex_tile.hex_object, 
                    "<Enter>", 
                    lambda e, q=q, r=r, hex_tile=hex_tile: self.on_hex_enter(e, q, r, hex_tile) #NOTE: lambda using optionals as otherwise broken
                    )
                """
                self.canvas.tag_bind(
                    hex_tile.hex_object, 
                    "<Leave>", 
                    lambda e, q=q, r=r, hex_tile=hex_tile: self.on_hex_leave(e, q, r, hex_tile) #NOTE: lambda using optionals as otherwise broken
                    )
                """

        return self.canvas



