##################################################
# RansackIt
#
# Written by Jacob Adams 
##################################################



##################################################
# Module imports
##################################################
import rescource

PLAYER_COLOURS = {
    0 : "#cf0000",
    1 : "#cfcf00",
    2 : "#00cf00",
    3 : "#0000cf",
    4 : "#cf00cf",
    5 : "#00cfcf"
    }


##################################################
# Player class
##################################################
class Player:
    def __init__(self, ID, name, inventory=rescource.Inventory):
        self.ID = ID
        self.name = name
        self.inventory = inventory

    def get_colour(self):
        return PLAYER_COLOURS[self.ID]