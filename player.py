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
    def __init__(self, ID, name, inventory=rescource.Inventory()):
        self.ID = ID
        self.name = name
        self.inventory = inventory

    def get_colour(self):
        return PLAYER_COLOURS[self.ID]
    
    def draw(self, canvas, x_origin, y_origin, box_width=128, box_height = 64, message="It's your turn!"):
        canvas.create_rectangle(x_origin, y_origin, x_origin+box_width, y_origin+box_height, fill="#a0a0a0")
        canvas.create_text(x_origin+(box_width//2), y_origin+(box_height//2)+6, text=self.name, fill=self.get_colour(), font=("Arial",12))
        canvas.create_text(x_origin+(box_width//2), y_origin+(box_height//2)-6, text=message, fill="black", font=("Arial",12))