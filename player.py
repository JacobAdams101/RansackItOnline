##################################################
# RansackIt
#
# Written by Jacob Adams 
##################################################



##################################################
# Module imports
##################################################

##################################################
# Inventory
##################################################
class Rescource:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Inventory:
    def __init__(self, name):
        self.name = name
        self.inventory = []

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


        





##################################################
# Player class
##################################################
class Player:
    def __init__(self, name):
        self.name = name