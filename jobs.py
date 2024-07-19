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
        leveled_up = False
        while self.lvl < 50 and self.xp >= self.xp_table[self.lvl -1]:
            self.lvl += 1
            leveled_up = True
        if leveled_up:
            self.statter()


    def statter(self):
        if self.lvl > 1:
            for key, value in self.stats.items():
                if key not in  ["Eva", "Luck", "HP", "MP"]:
                    self.stats[key] += rd.randint(0,2) * self.lvl




        






class WhiteMage(Levels):
    def __init__(self, name, race, xp=0, lvl=1):
        if not name:
            raise ValueError("Missing name for Char")
        self.name = name
        
        if not race:
            raise ValueError("Missing race for Char")
        self.race = race

        super().__init__(xp, lvl)
        self.skills = ["Attack", "Cure", "Holy", "Block", "Item"]
        self.inv = ["Lembas"]
        self.block = False
        self.stats = {
            "HP": 50, 
            "HPMax": 50,
            "MP": 100,
            "MPMax": 100,
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
        self.inv = ["Lembas"]
        self.block = False
        self.stats = {
            "HP": 40,
            "HPMax": 40,
            "MP": 120,
            "MPMax": 120,
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
        self.inv = ["Lembas"]
        self.block = False
        self.stats = {
            "HP": 150,
            "HPMax": 150,
            "MP": 20,
            "MPMax": 20,
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
        self.inv = ["Lembas"]
        self.block = False
        self.stats = {
            "HP": 70,
            "HPMax": 70,
            "MP": 10,
            "MPMax": 10,
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
        self.inv = ["Lembas"]
        self.block = False
        self.stats = {
            "HP": 60,
            "HPMax": 60,
            "MP": 20,
            "MPMax": 20,
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
        self.block = False
        self.stats = {
            "HP": 50, 
            "MP": 0,
            "Str": 50,    
            "Int": 0,
            "Def": 20, 
            "Spi": 20,
            "Spd": 15,
            "Eva": 5,
            "Luck": 5,
        }

    

class ChaosDwarf:
    def __init__(self):
        self.name = "Chaos Dwarf"
        self.skills = ["Attack", "Block"]
        self.block = False
        self.stats = {
            "HP": 250, 
            "MP": 0,
            "Str": 120,    
            "Int": 0,
            "Def": 120, 
            "Spi": 120,
            "Spd": 20,
            "Eva": 5,
            "Luck": 5,
        }



class ChaosElf:
    def __init__(self):
        self.name = "Chaos Elf"
        self.skills = ["Attack", "Block"]
        self.block = False
        self.stats = {
            "HP": 200, 
            "MP": 0,
            "Str": 100,    
            "Int": 0,
            "Def": 100, 
            "Spi": 100,
            "Spd": 35,
            "Eva": 25,
            "Luck": 5,
        }






class Easterling:
    def __init__(self):
        self.name = "Easterling"
        self.skills = ["Attack", "Block"]
        self.block = False
        self.stats = {
            "HP": 80, 
            "MP": 0,
            "Str": 65,    
            "Int": 0,
            "Def": 50, 
            "Spi": 40,
            "Spd": 20,
            "Eva": 15,
            "Luck": 5,
        }







class Wight:
    def __init__(self):
        self.name = "Wight"
        self.skills = ["Attack", "Block"]
        self.block = False
        self.stats = {
            "HP": 100, 
            "MP": 0,
            "Str": 40,    
            "Int": 0,
            "Def": 50, 
            "Spi": 50,
            "Spd": 25,
            "Eva": 50,
            "Luck": 5,
        }









class Spider:
    def __init__(self):
        self.name = "Spider"
        self.skills = ["Attack", "Block"]
        self.block = False
        self.stats = {
            "HP": 80, 
            "MP": 0,
            "Str": 50,    
            "Int": 0,
            "Def": 60, 
            "Spi": 30,
            "Spd": 30,
            "Eva": 25,
            "Luck": 5,
        }
class OrcCap:
    def __init__(self):
        self.name = "Orc Captain"
        self.skills = ["Attack", "Block"]
        self.block = False
        self.stats = {
            "HP": 700, 
            "MP": 0,
            "Str": 200,    
            "Int": 0,
            "Def": 120, 
            "Spi": 120,
            "Spd": 40,
            "Eva": 10,
            "Luck": 5,
        }
class Watcher:
    def __init__(self):
        self.name = "Watcher"
        self.skills = ["Attack", "Block"]
        self.block = False
        self.stats = {
            "HP": 3000, 
            "MP": 0,
            "Str": 350,    
            "Int": 0,
            "Def": 200, 
            "Spi": 30,
            "Spd": 999,
            "Eva": 25,
            "Luck": 15,
        }
class Warg:
    def __init__(self):
        self.name = "Warg"
        self.skills = ["Attack", "Block"]
        self.block = False
        self.stats = {
            "HP": 200, 
            "MP": 0,
            "Str": 80,    
            "Int": 0,
            "Def": 80, 
            "Spi": 80,
            "Spd": 35,
            "Eva": 20,
            "Luck": 5,
        }
