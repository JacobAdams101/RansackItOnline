##################################################
# RansackIt
#
# Written by Jacob Adams 
##################################################



##################################################
# Module imports
##################################################

import player

BUILDING_RADIUS = 6

def draw_building(canvas, x, y, colour, text, unit_radius=BUILDING_RADIUS):
    POINTS = [
        x-unit_radius, y+unit_radius,
        x+unit_radius, y+unit_radius, 
        x+unit_radius, y-unit_radius, 
        x, y-unit_radius-2, 
        x-unit_radius, y-unit_radius,
        ]
    unit_object = canvas.create_polygon(POINTS, outline="black", fill=colour, width=1)
    #unit_object = canvas.create_rectangle(x-unit_radius, y-unit_radius, x+unit_radius, y+unit_radius, outline="black", fill=colour)
    unit_text_object = canvas.create_text(x, y, text=text, fill="black", font=("Arial",8))
    return unit_object, unit_text_object


class Building:
    def __init__(self, owner_ID):
        self.owner_ID = owner_ID
        self.building_colour = player.PLAYER_COLOURS[owner_ID]

    def draw(self, canvas, x, y):
        return draw_building(canvas, x, y, self.building_colour, "NA")


class Road(Building):
    def __init__(self, owner_ID, hex_1, hex_2):
        super().__init__(owner_ID)

        self.hex_1 = hex_1
        self.hex_2 = hex_2

    def get_pop(self):
        return 0
    
    def draw(self, canvas, x, y):
        return draw_building(canvas, x, y, self.building_colour, "R")


class Village(Building):
    def __init__(self, owner_ID):
        super().__init__(owner_ID)

    def get_dice(self):
        return 6
    
    def get_pop(self):
        return 1
    
    def draw(self, canvas, x, y):
        return draw_building(canvas, x, y, self.building_colour, "V")

class Town(Building):
    def __init__(self, owner_ID):
        super().__init__(owner_ID)

    def get_dice(self):
        return 10
    
    def get_pop(self):
        return 2
    
    def draw(self, canvas, x, y):
        return draw_building(canvas, x, y, self.building_colour, "T")

class City(Building):
    def __init__(self, owner_ID):
        super().__init__(owner_ID)

    def get_dice(self):
        return 10
    
    def get_pop(self):
        return 2
    
    def draw(self, canvas, x, y):
        return draw_building(canvas, x, y, self.building_colour, "C")