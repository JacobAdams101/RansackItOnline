##################################################
# RansackIt
#
# Written by Jacob Adams 
##################################################



##################################################
# Module imports
##################################################


class Building:
    def __init__(self, owner_ID):
        self.owner_ID = owner_ID


class Road(Building):
    def __init__(self, owner_ID, hex_1, hex_2):
        super().__init__(owner_ID)

        self.hex_1 = hex_1
        self.hex_2 = hex_2

    def get_pop(self):
        return 0


class Village(Building):
    def __init__(self, owner_ID):
        super().__init__(owner_ID)

    def get_dice(self):
        return 6
    
    def get_pop(self):
        return 1

class Town(Building):
    def __init__(self, owner_ID):
        super().__init__(owner_ID)

    def get_dice(self):
        return 10
    
    def get_pop(self):
        return 2

class City(Building):
    def __init__(self, owner_ID):
        super().__init__(owner_ID)

    def get_dice(self):
        return 10
    
    def get_pop(self):
        return 2