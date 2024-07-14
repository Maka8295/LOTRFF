import sys
import random as rd

class Levels:
    def __init__(self, xp=0, lvl=1):
        self.lvl = lvl
        self.xp = xp
    
        self.xp_table = [int(100 * (1.1 ** i)) for i in range(49)]
    
        for i in range(1, len(self.xp_table)):
            self.xp_table[i] += self.xp_table[i - 1]
    
    def leveler(self, xp_gained):
        self.xp += xp_gained
        if self.lvl < 50:
            for val in self.xp_table:
                if self.xp >= val:
                    self.lvl = self.xp_table.index(val) + 2







        






class WhiteMage(Levels):
    def __init__(self, name, race, xp=0, lvl=1):
        if not name:
            raise ValueError("Missing name for Char")
        self.name = name
        
        if not race:
            raise ValueError("Missing race for Char")
        self.race = race

        super().__init__(xp, lvl)
        self.skills = ["Attack", "Cure", "Block", "Item"]
        self.stats = {
            "HP": 50, 
            "MP": 100,
            "Str": 10,    
            "Int": 100,
            "Def": 20, 
            "Spi": 100,
            "Spd": 20,
            "Eva": 10,
            "Luck": 5,
        }

class BlackMage(Levels):
    def __init__(self, name, race, xp=0, lvl=1):
        if not name:
            raise ValueError("Missing name for Char")
        self.name = name
        
        if not race:
            raise ValueError("Missing race for Char")
        self.race = race

    
        super().__init__(xp, lvl) 

        self.skills = ["Attack", "Fire", "Ice", "Lightning", "Block", "Item"]
        self.stats = {
            "HP": 40, 
            "MP": 120,
            "Str": 5,    
            "Int": 120,
            "Def": 20, 
            "Spi": 80,
            "Spd": 20,
            "Eva": 10,
            "Luck": 10,
        }

class Knight(Levels):
    def __init__(self, name, race, xp=0, lvl=1):
        if not name:
            raise ValueError("Missing name for Char")
        self.name = name
        
        if not race:
            raise ValueError("Missing race for Char")
        self.race = race


        super().__init__(xp,lvl)
 
        self.skills = ["Attack", "Block", "Item"]
        self.stats = {
            "HP": 150, 
            "MP": 20,
            "Str": 120,    
            "Int": 20,
            "Def": 150, 
            "Spi": 60,
            "Spd": 10,
            "Eva": 5,
            "Luck": 5,
        }

class Burglar(Levels):
    def __init__(self, name, race, xp=0, lvl=1):
        if not name:
            raise ValueError("Missing name for Char")
        self.name = name
        
        if not race:
            raise ValueError("Missing race for Char")
        self.race = race

  
        super().__init__(xp,lvl)

        self.skills = ["Attack", "Steal", "Block", "Item"]
        self.stats = {
            "HP": 70, 
            "MP": 10,
            "Str": 70,    
            "Int": 20,
            "Def": 40, 
            "Spi": 40,
            "Spd": 40,
            "Eva": 30,
            "Luck": 20,
        }

class Bard(Levels):
    def __init__(self, name, race, xp=0, lvl=1):
        if not name:
            raise ValueError("Missing name for Char")
        self.name = name
        
        if not race:
            raise ValueError("Missing race for Char")
        self.race = race

 
        super().__init__(xp,lvl)

        self.skills = ["Attack", "Song", "Block", "Item"]
        self.stats = {
            "HP": 60, 
            "MP": 20,
            "Str": 65,    
            "Int": 20,
            "Def": 40, 
            "Spi": 80,
            "Spd": 30,
            "Eva": 40,
            "Luck": 10,
        }

class Orc:
    def __init__(self):
        self.name = "Orc"
        self.skills = ["Attack", "Block"]
        self.stats = {
            "HP": 50, 
            "MP": 0,
            "Str": 20,    
            "Int": 0,
            "Def": 20, 
            "Spi": 20,
            "Spd": 15,
            "Eva": 5,
            "Luck": 5,
        }

    

class ChaosDwarf:
    ...
class ChaosElf:
    ...
class Easterling:
    ...
class Wight:
    ...
class Spider:
    ...
class OrcCap:
    ...
class Watcher:
    ...
class Warg:
    ...

