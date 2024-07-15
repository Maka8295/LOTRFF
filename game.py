import story
import jobs
import random as rd
import sys

def attack(user, target): #calculates damage based on user
    ev_rate = target.stats["Eva"] / 100
    roll = rd.random()
    if roll > ev_rate:
        dmg_reduction = target.stats["Def"] / 2
        if target.block == False:
            dmg = user.stats["Str"] + rd.randint(-5,5) - dmg_reduction
        else:
            dmg = (user.stats["Str"] + rd.randint(-5,5) - dmg_reduction) / 2 
        if dmg < 0:
            return 0
        else:
            return dmg
    else:
        return 0

#def magic(user):
    

#def cure()

def campsite(party, tents):
    print(story.campsitestory)
    ans = input()
    if ans == "n" or ans == "N":
        return party, tents
    else:
        return rest(party, tents)


def rest(party, tents): # returns healed party and tents - 1
    for member in party:
        member.stats["HP"] = member.stats["HPMax"]
        member.stats["MP"] = member.stats["MPMax"]
    tents -= 1
    return party, tents


def encounter(party): #return [party, gil_spawn, xp_spawn]

    orc = jobs.Orc()
    chaos_dwarf = jobs.ChaosDwarf()
    chaos_elf = jobs.ChaosElf()
    wight = jobs.Wight()
    spider = jobs.Spider()
    orc_cap = jobs.OrcCap()
    watcher = jobs.Watcher()
    warg = jobs.Warg()

    enemy_no = rd.randint(1,4)
    enemies =  [orc]
    spawn = []
    turn_order = []
    for i in range(enemy_no):
        spawn.append(rd.choice(enemies))
    
    gil_spawn = len(spawn) * 100 + rd.randint(-20,20)
    xp_spawn = len(spawn) * 20 + rd.randint(-20,20)

    turn_order.extend(party)
    turn_order.extend(spawn)
    turn_order = sorted(turn_order, key=lambda character: character.stats["Spd"], reverse=True)


    active_party = []
    active_party.extend(party)
    print("************************************************************")
    for _ in spawn:
        print(_.name," ", end="")
    print(f"have attacked your party!")
    print("************************************************************\n")
    while True:

        for turn in turn_order:
            if not spawn:
                print(f"You recieve {gil_spawn} gil and each member of your party recieves {xp_spawn} EXP!\n") 
                return [party, gil_spawn, xp_spawn]
            if not active_party:
                sys.exit("Oh dear your party is dead!")  

            if turn in spawn:
                turn.block = False
                en_action = rd.choice(turn.skills)
                if en_action == "Block":
                    turn.block = True #to do
                
                if en_action == "Attack":
                    en_target = rd.choice(active_party)
                    en_dmg = attack(turn, en_target)
                    en_target.stats["HP"] -= en_dmg
                    print(f"{turn.name} uses {en_action} on {en_target.name} dealing {en_dmg} damage!\n")
                    if en_target.stats["HP"] <= 0:
                        en_target.stats["HP"] = 0
                        active_party.remove(en_target)
                        print(f"{en_target.name} has been defeated!\n")

            elif turn in active_party and turn.stats["HP"] > 0:
                block = False
                print("~~~")
                for member in party:
                    print(f"{member.name} - HP: {member.stats['HP']} - MP: {member.stats['MP']}")
                print("~~~\n")
                while True:
                    action = input(f"What will {turn.name} do?\n{turn.skills}\n\n")
                    if action in turn.skills:
                        break
                    print("\nInvalid selection!\n")
                
                if action == "Block":
                    turn.block = True
                if action == "Item":
                    continue
                if action == "Fire":
                    continue
                if action == "Ice":
                    continue
                if action == "Lightning":
                    continue
                if action == "Song":
                    continue
                if action == "Steal":
                    continue

                if action == "Attack":
                    while True:
                        target = input("Select Target:\n")  # if two orcs, first orc in turn order is targeted
                        selected_target = None
                        for target_char in spawn:
                            if target == target_char.name:
                                selected_target = target_char
                                dmg = attack(turn, selected_target)
                                break
                        if selected_target:
                            selected_target.stats["HP"] -= dmg
                            print(f"{turn.name} deals {dmg} damage to {selected_target.name}")
                            if selected_target.stats["HP"] <= 0:
                                selected_target.stats["HP"] = 0
                                spawn.remove(selected_target)
                            break
                        else:
                            print("Invalid target!\n")               


def shop(party, gil, tents):  #returns list with [party, gil, tents] 
    merchant = story.dynamicstory()
    print(f"{merchant[0]}\n")
    print("What will it be then?\n")
    partynames = []
    for mem in party:
        partynames.append(mem.name)  
    while True:
        if "dwarf" in merchant[0]: 
            print("~~~\nSword of Belegost - 500 Gil ### Mithril Tipped Arrows - 300 Gil ### Mead - 100 Gil ### Tent - 50 Gil\n~~~")
            print(f"$$$ Current Gil: {gil} $$$\n")
            choice = input("Enter name of item or 'n' to quit and or return to previous menu: ")    
            if choice == "n" or choice == "N":
                return [party, gil, tents]
############# this logic encompuses one item!! #####################
            elif choice == "Sword of Belegost" and gil >= 500:
                target = input("Who will equip this? ")
                while True:
                    if target in partynames:
                        for mem in party:
                            if target == mem.name:
                                mem.stats["Str"] += 30
                                gil -= 500
                        break

                    elif target == "n" or target == "N":
                        break
                    else:
                        print("\nWho's that?")
                        break
                        
                        
            elif choice == "Sword of Belegost" and gil < 500:
                print("\nYou cant afford that!")
####################################################################          
            elif choice == "Mithril Tipped Arrows" and gil >= 300:
                target = input("Who will equip this? ")
                while True:
                    if target in partynames:
                        for mem in party:
                            if target == mem.name:
                                mem.stats["Str"] += 20
                                gil -= 300
                        break

                    elif target == "n" or target == "N":
                        break
                    else:
                        print("\nWho's that?")
                        break
                        
                        
            elif choice == "Mithril Tipped Arrows" and gil < 300:
                print("\nYou cant afford that!")
######################################################################
            elif choice == "Mead" and gil >= 100:
                target = input("Who will hold this? ")
                while True:
                    if target in partynames:
                        for mem in party:
                            if target == mem.name:
                                mem.inv.append("Mead")
                                gil -= 100
                        break

                    elif target == "n" or target == "N":
                        break
                    else:
                        print("\nWho's that?")
                        break
                        
                        
            elif choice == "Mead" and gil < 100:
                print("\nYou cant afford that!")
######################################################################
############# this logic encompuses TENT ! #####################
            elif choice == "Tent" and gil >= 50:
                tents += 1
                gil -= 50

                        
                        
            elif choice == "Tent" and gil < 50:
                print("\nYou cant afford that!")
####################################################################  


            else:
                print(f"\nI don't have any {choice}!")
#########################END OF DWARF MERCHANT######################
        elif "elf" in merchant[0]:
            print("~~~\nJewel Crested Staff ### Lembas ### Ether\n~~~")

        elif "hat" in merchant[0]:
            print("~~~\nMagic Mushrooms ### Old Took\n~~~")

    

















def main():
    party = []
    creation_names = []
    gil = 0
    tents = 1

    print(story.story1)

    for _ in range(4): 
        while True:
            name = input("What is the name of this character? ")
            if name not in creation_names:
                creation_names.append(name)
                break
            print("\nThat character already exists!\n")
        
        print("\nRaces: ~~~ Man, Elf, Dwarf, Hobbit ~~~\n")
        while True:
            race = input("What race is this character? ")
            if race in ["Man", "Elf", "Dwarf", "Hobbit", "Maia"]:
                break
            else:
                print("That race does not exist!")
   
        print("\nJobs: ~~~ White Mage, Black Mage, Knight, Burglar, Bard ~~~\n")
    
        while True:
            job = input("What is his or her job? ")
            if job in ["White Mage", "Black Mage", "Knight", "Burglar", "Bard"]:
                break
            else:
                print("That job does not exist!")
    
        if job == "White Mage":
            char = jobs.WhiteMage(name, race)
        elif job == "Black Mage":
            char = jobs.BlackMage(name, race)
        elif job == "Knight":
            char = jobs.Knight(name, race)
        elif job == "Burglar":
            char = jobs.Burglar(name, race)
        elif job == "Bard":
            char = jobs.Bard(name, race)
    
        party.append(char)
        print("\n~~~ Current Party Members ~~~")
        for person in party:
            print(f"{person.name}  ",end="")
        
        if len(party) == 4:
            break
        ans = input("\n\nWould you like to make another character? Y/n\n")
        if ans == "n" or ans == "N":
            break
        
    if len(party) == 4:
        print(f"\n{party[0].name}, {party[1].name}, {party[2].name} and {party[3].name} set", end ="")
    elif len(party) == 3:
        print(f"\n{party[0].name}, {party[1].name}, and {party[2].name} set", end = "")
    elif len(party) == 2:
        print(f"\n{party[0].name} and {party[1].name} set", end="")
    else:
        print(f"\n{party[0].name} sets", end="")
    print(story.story2) 

    ##### This is one encounter #####
    loot = encounter(party) #important to equate party, to update HP values etc   
    party = loot[0]
    gil += loot[1]
    for member in party:
        member.leveler(loot[2])   #change this multiplier to adjust xp rates
        member.statter()
        member.block = 0 #reset block states
        print(f"{member.name} is level {member.lvl} and has {member.xp} EXP")
    ##################################    
   
    print("\nYour party continues south...\n")
    
    ###########################
    party, gil, tents = shop(party, gil, tents)

    campsite(party, tents)
    


    



main() 

