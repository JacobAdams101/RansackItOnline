##################################################
# RansackIt
#
# Written by Jacob Adams 
##################################################



##################################################
# Module imports
##################################################

#Basic Rescources
RESCOURCE_FOOD = "FOOD"
RESCOURCE_WOOD = "WOOD"
RESCOURCE_BRICK = "BRICK"
RESCOURCE_ORE = "ORE"

#Commodities
RESCOURCE_SPICE = "SPICE"
RESCOURCE_PAPER = "PAPER"
RESCOURCE_MARBLE = "MARBLE"
RESCOURCE_GUNPOWDER = "GUNPOWDER"

#Money
RESCOURCE_COIN = "COIN"


##################################################
# Inventory
##################################################
class Rescource:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Inventory:
    def __init__(
            self, 
            inventory=[Rescource(RESCOURCE_FOOD, 2), Rescource(RESCOURCE_WOOD, 2), Rescource(RESCOURCE_BRICK, 2), Rescource(RESCOURCE_COIN, 2)]
            ):
        self.inventory = inventory

    def add(self, rescources=[]):
        for r in rescources:
            matched = False
            for i in self.inventory:
                if i.name == r.name:
                    i.amount += r.amount
                    matched = True
                    break
            if not matched:
                self.inventory.append(r)
    
    def _min_set_(self, rescources=[]):
        new_set = []
        for r in rescources:
            matched = False
            for i in new_set:
                if i.name == r.name:
                    i.amount += r.amount
                    matched = True
                    break
            if not matched:
                new_set.append(r)
        
        return new_set

    def contains(self, rescources=[]):
        rescources = self._min_set_(rescources)
        for r in rescources:
            matched = False
            for i in self.inventory:
                if i.name == r.name:
                    matched = i.amount >= r.amount
                    break
            if not matched:
                return False
        return True
    
    def remove(self, rescources=[]):
        if not self.contains(rescources=rescources):
            return False
        
        for r in rescources:
            matched = False
            for i in self.inventory:
                if i.name == r.name:
                    i.amount -= r.amount
                    matched = True
                    break
            if not matched:
                self.inventory.append(r)

        i = 0 
        while i < len(self.inventory):
            item = self.inventory[i]
            if item.amount == 0:
                del self.inventory[i]
            else:
                i += 1
    
    def draw(self, canvas, x_origin, y_origin, box_size = 64, step_size = 10):
        for i, r in enumerate(self.inventory):
            x = i * (box_size+step_size) + x_origin
            y = y_origin
            canvas.create_rectangle(x, y, x+box_size, y+box_size, fill="#a0a0a0")
            canvas.create_text(x+(box_size//2), y+(box_size//2)+6, text=r.name, fill="black", font=("Arial",12))
            canvas.create_text(x+(box_size//2), y+(box_size//2)-6, text=r.amount, fill="black", font=("Arial",12))