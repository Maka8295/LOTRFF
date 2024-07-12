import sys
import random as rd
import time

class Stats:

    def __init__(self, HP, MP, Str, Int, Def, Spirit, Luck, Speed):

        self.HP = HP

        self.MP = MP

        self.Str = Str

        self.Int = Int

        self.Def = Def

        self.Spirit = Spirit

        self.Luck = Luck

        self.Speed = Speed

 

    def race_modifiers(self, race):

        if race == "Elf":

            self.HP -= 5

            self.MP += 5

            self.Int += 5

            self.Def -= 5

            self.Spirit += 5

            self.Luck -= 5

            self.Speed += 5

        elif race == "Man":

            self.HP += 5

            self.MP -= 10

            self.Spirit -= 10

            self.Def += 5

            self.Str += 10

        elif race == "Dwarf":

            self.HP += 20

            self.MP -= 15

            self.Str += 10

            self.Def += 10

            self.Int -= 15

            self.Spirit += 10

            self.Speed -= 5   

        elif race == "Hobbit":

            self.HP -= 20

            self.MP -= 10

            self.Str -= 20

            self.Def -= 20

            self.Int += 10

            self.Spirit -= 5

            self.Speed += 20

            self.Luck += 40

        elif race == "Maia":

            self.HP += 20

            self.MP += 50

            self.Int += 50

            self.Spirit += 25       

 

job_stats = {

    "White Mage": Stats(50, 100, 10, 50, 20, 100, 5, 20),

    "Black Mage": Stats(40, 120, 5, 120, 10, 50, 10, 20),

    "Knight": Stats(150, 20, 120, 20, 150, 50, 5, 10),

    "Burglar": Stats(70, 10, 70, 20, 40, 40, 20, 40),

}

 

job_skills = {

    "White Mage": ["Attack", "Block", "Cure", "Item"],

    "Black Mage": ["Attack", "Block", "Fire", "Item"],

    "Knight": ["Attack", "Block", "Item"],

    "Burglar": ["Attack", "Block", "Steal", "Item"],

}

 

class Character:

    def __init__(self, name):

        self.name = name

        self.stats = None

        self.job = None

        self.race = None

        self.skills = None

        self.item = None

        self.xp = None

        self.lvl = None


orc = Character("Orc")
orc.stats = Stats(70, 0 , 20, 0, 30, 30, 5, 10)
orc.skills = ["Attack"]


cDwarf = Character("Chaos Dwarf")

cElf = Character("Chaos Elf")

easter = Character("Easterling")

wight = Character("Wight")

warg = Character("Warg")

spider = Character("Spider")

orcCap = Character("Orc Captain")



watcher = Character("Watcher of the Depths")
watcher.stats = Stats(1200, 300 , 50, 50, 50, 50, 10, 15)
watcher.skills = ["Attack","Fire"]















party = []

print("Elrond, Lord of Imladris has entrusted your party with a dangerous quest.\nYou are to investigate reports of strange sightings at the base of the mountains of Celebdil.\nWho is departing on this quest?\n") 

for i in range(4):

    character = Character(input("Enter name: "))
    character.lvl = 1
    character.xp = 0 

    while True:

        character.job = (input("Choose your job:\n\nWhite Mage\nBlack Mage\nKnight\nBurglar\n\n"))

        if character.job in job_stats:

            character.stats = job_stats[character.job]

            break

        print("That job doesn't exist!\n")

 

    if character.job in job_skills:

        character.skills = job_skills[character.job]

 

    while True:

        character.race = (input("\nWhat race are you?\n\nElf\nMan\nDwarf\nHobbit\n\n"))

        if character.race in ["Elf", "Maia", "Man", "Hobbit", "Dwarf"]:

            character.stats.race_modifiers(character.race)

            break

        print("That race doesn't exist!\n")

 

 

   #if (character.name == "Bilbo" or character.name =="Frodo") and character.race == "Hobbit":
        #character.skills.append("Invisibility")

    #elif character.name == "Gandalf" and character.race == "Maia":
        #character.skills.append("Fire of Anor")

        #elif character.name == "Gimli" and character.race == "Dwarf":
    #character.skills.append("Toss me!")

        #elif character.name == "Cloud" and character.job == "Knight":
        #character.skills.append("Omnislash")

        #elif character.name == "Legolas" and character.race == "Elf":
        #character.skills.append("Double Strike")

        #elif character.name == "Aragorn" and character.race == "Man":
        #character.skills.append("Blessings of Elrond")

 

   

    party.append(character)

    if len(party) == 1:

        print(f"Current Party Members: {party[0].name}\n")

    elif len(party) == 2:

        print(f"Current Party Members: {party[0].name}, {party[1].name}\n")

    elif len(party) == 3:

        print(f"Current Party Members: {party[0].name}, {party[1].name}, {party[2].name}\n")

    else:

        print(f"Current Party Members: {party[0].name}, {party[1].name}, {party[2].name}, {party[3].name}\n")

   

    

    if i < 3:

        while True:

            morechar = input(f"Party: [{len(party)}/4] Do you want to make another character? Y/N: ")

            if morechar == "N":

                break

            elif morechar == "Y":

                break

            else:

                print("Invalid input...\n")

        if morechar == "N":

            break

 
if len(party) == 4:
    print(f"\n{party[0].name}, {party[1].name}, {party[2].name} and {party[3].name} set", end ="")
elif len(party) == 3:
    print(f"\n{party[0].name}, {party[1].name}, and {party[2].name} set", end = "")
elif len(party) == 2:
    print(f"\n{party[0].name} and {party[1].name} set", end="")
else:
    print(f"\n{party[0].name} sets", end="")
print(" out from Imladris, horses laden with lembas and supplies have been gifted to the party from Lord Elrond.\n The party makes south, following the edge of the Misty Mountains.\n")



def encounter():
    enemy_no = rd.randint(1,4)
    enemies =  [orc]
    spawn = []
    turn_order = []
    for i in range(enemy_no):
        spawn.append(rd.choice(enemies))
    
    turn_order.extend(party)
    turn_order.extend(spawn)

    turn_order = sorted(turn_order, key =lambda character: character.stats.Speed, reverse=True)
    active_party = []
    active_party.extend(party)
    

    for _ in spawn:
        print(_.name," ", end="")
    print(f"have attacked your party!\n\n")
    
    while True:
        for char in turn_order:
            if char in enemies:
                en_action = rd.choice(char.skills)   #NEED TO REMOVE BLOCK FOR NOW!
                if en_action == "Block":
                    ...
                if en_action == "Attack":
                    en_target = rd.choice(active_party)
                    en_dmg = vars(char.stats)["Str"] + rd.randint(-5,5)
                    vars(en_target.stats)["HP"] -= en_dmg

                    if vars(en_target.stats)["HP"] < 0:
                        active_party.remove(en_target)

                print(f"{char.name} uses {en_action} on {en_target.name} dealing {en_dmg} damage!\n")
            
            elif char in active_party: #start of player turn #turn is skipped if not in active
                #print all party members HP:
                for member in party: #want to list even in-active party mems
                    print(f"{member.name} - HP: {vars(member.stats)['HP']}, MP: {vars(member.stats)['MP']}")

                while True:
                    action = input(f"What will {char.name} do?\n{char.skills}\n\n")
                    if action in char.skills:
                        break
                    print("\nInvalid selection!\n")
                
                if action == "Attack":
                    dmg = vars(char.stats)["Str"] + rd.randint(-5,5)
                    while True:
                        target = input("Select Target:\n")  # if two orcs, first orc in turn order is targeted
                        selected_target = None
                        for target_char in spawn:
                            if target == target_char.name:
                                selected_target = target_char
                                break
                
                        if selected_target:
                            vars(selected_target.stats)["HP"] -= dmg
                            print(f"{char.name} deals {dmg} damage to {selected_target.name}")
                            if vars(selected_target.stats)["HP"] < 0:
                                spawn.remove(selected_target)
                            break
                        else:
                            print("Invalid target!\n")


                elif action == "Fire":
                    ...
                
                elif action == "Block":
                    ...
                
                elif action == "Cure":
                    ...                    
    
                elif action == "Item":
                    ...

        if not active_party:
            sys.exit("Oh dear, your party is dead!")
        elif not spawn:
            print("Enemies defeated!")
            break
encounter()
#HP, MP, Str, Int, Def, Spirit, Luck, Speed
#print(vars(orc.stats)["HP"])

#print(vars(character.stats))

#print(character.name)

#print(character.job)

#print(character.skills)

#print(character.race)

 

