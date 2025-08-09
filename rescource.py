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
            name, 
            inventory=[Rescource(RESCOURCE_FOOD, 2), Rescource(RESCOURCE_WOOD, 2), Rescource(RESCOURCE_BRICK, 2), Rescource(RESCOURCE_COIN, 2)]
            ):
        self.name = name
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