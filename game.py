import story
import jobs
import random as rd
import sys

def attack(user, target): #calculates damage based on user
    ev_rate = target.stats["Eva"] / 100
    crit_rate = user.stats["Luck"] / 100
    crit = False
    roll = rd.random()
    crit_roll = rd.random()
    if crit_roll < crit_rate:
        crit = True
    if roll > ev_rate:
        dmg_reduction = target.stats["Def"] / 2
        if target.block == False:
            if crit == False:
                dmg = user.stats["Str"] + rd.randint(-5,5) - dmg_reduction
            else:
                dmg = user.stats["Str"] * 2 + rd.randint(-20,20) - dmg_reduction
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

def item():
    ...

def campsite(party, tents):
    print(story.campsitestory)
    print(f"\nNumber of tents: {tents}\n")
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

def turn_orderer(turn_order): # takes in raw turn order, then sorts according to speed and returns
    return sorted(turn_order, key=lambda character: character.stats["Spd"], reverse=True)

def encounter(party, gil, enemies): #return [party, new gill amt, xp gained]
    enemy_no = rd.randint(1,4)
    spawn = []
    turn_order = []
    for i in range(enemy_no):
        spawn.append(rd.choice(enemies))
    
    gil_spawn = len(spawn) * 100 + rd.randint(-20,20)
    gil += gil_spawn
    xp_spawn = len(spawn) * 50 + rd.randint(-20,20)

    turn_order.extend(party)
    turn_order.extend(spawn)
    turn_order = turn_orderer(turn_order)

    active_party = []
    active_party.extend(party)
    print("[!][!][!] Your party has been attacked [!][!][!]\n")
    while True:


        for turn in turn_order:
            active_party_names = []
            for mem in active_party:
                active_party_names.append(mem.name) 

            if not spawn:
                print(f"You recieve {gil_spawn} gil and each member of your party recieves {xp_spawn} EXP!\n") 
                return [party, gil, xp_spawn]
            if not active_party:
                sys.exit("Oh dear your party is dead!")  

            if turn in spawn:
                turn.block = False
                en_action = rd.choice(turn.skills)
                if en_action == "Block":
                    turn.block = True #to do
                    print(f"{turn.name} blocks!\n" )

                
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
                print("**************************ENEMIES***************************")
                for _ in spawn:
                    print(_.name," ", end="")
                print("\n**************************ENEMIES***************************\n")

                block = False
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~PARTY~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                for member in party:
                    print(f"{member.name} - HP: {member.stats['HP']} - MP: {member.stats['MP']}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~PARTY~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                
                
                while True:
                    action = input(f"What will {turn.name} do?\n{turn.skills}\n\n")
                    if action in turn.skills:
                        break
                    print("\nInvalid selection!\n")
                
                if action == "Block":
                    turn.block = True
                if action == "Item":
                    print(turn.inv)
                    while True:
                        used_item = False
                        if used_item == True:
                            break
                        selection = input("Select item or 'n' to go back: ")
                        if selection in turn.inv:
                            turn.inv.remove(selection)
                            if selection == "Lembas":
                                while True:
                                    lembas_target = input("Select target: ")
                                    if lembas_target in active_party_names:
                                        break
                                    print("Invalid target!\n")
                                for mem in active_party:
                                    if mem.name == lembas_target:
                                        mem.stats["HP"] += 100
                                        if mem.stats["HP"] > mem.stats["HPMax"]:
                                            mem.stats["HP"] = mem.stats["HPMax"]
                                        print(f"\n{turn.name} uses Lembas on {lembas_target} healing 100 HP!")
                                        used_item = True
                                        break
                            if selection == "Ether":
                                while True:
                                    ether_target = input("Select target: ")
                                    if ether_target in active_party_names:
                                        break
                                    print("Invalid target!\n")
                                for mem in active_party:
                                    if mem.name == ether_target:
                                        mem.stats["MP"] += 100
                                        if mem.stats["MP"] > mem.stats["MPMax"]:
                                            mem.stats["MP"] = mem.stats["MPMax"]
                                        print(f"\n{turn.name} uses an Ether on {ether_target} restoring 100 MP!")
                                        used_item = True
                                        break                          



                            if selection == "Mead":
                                while True:
                                    mead_target = input("Select target: ")
                                    if mead_target in active_party_names:
                                        break
                                    print("Invalid target!\n")
                                for mem in active_party:
                                    if mem.name == mead_target:
                                        mem.stats["HP"] += 60
                                        if mem.stats["HP"] > mem.stats["HPMax"]:
                                            mem.stats["HP"] = mem.stats["HPMax"]
                                        print(f"\n{turn.name} uses Mead on {mead_target} healing 60 HP!")
                                        used_item = True
                                        break

                            
                        elif selection == 'n' or selection == 'N':
                            break
                        else:
                            print("That item doesn't exist!\n")


                if action == "Fire":
                    continue
                if action == "Ice":
                    continue
                if action == "Lightning":
                    continue
                if action == "Song":
                    if turn.stats["MP"] >= 5:
                        songheal = turn.stats["Int"] + rd.randint(-5,5)
                        turn.stats["MP"] -= 5
                        for mem in active_party:
                            if mem.stats["HP"] + songheal >= mem.stats["HPMax"]:
                                mem.stats["HP"] = mem.stats["HPMax"]
                            else:
                                mem.stats["HP"] += songheal
                        print(f"{turn.name} sings a song, the party is healed by {songheal} HP!\n")
                    else:
                        print("Not enough MP!\n")
                if action == "Steal":
                    steal_target = rd.choice(spawn)
                    steal_gil = rd.randint(0, turn.stats["Spd"] * 10)
                    gil += steal_gil
                    print(f"{turn.name} steals {steal_gil} Gil from {steal_target.name}!\n")
                
                if action == "Holy":
                    while True:
                        target = input("Select Target: ")
                        selected_target = None
                        for target_char in spawn:
                            if (target == "Wight" or target == "Chaos Elf" or target == "Chaos Dwarf") and target_char.name == target:
                                selected_target = target_char
                                break
                        if selected_target:
                            spawn.remove(selected_target)
                            print(f"{turn.name} smites {selected_target.name}!\n")
                            break
                        else:
                            print("Invalid target!\n")
                            break



                if action == "Attack":
                    while True:
                        target = input("Select Target: ")  # if two orcs, first orc in turn order is targeted
                        selected_target = None
                        for target_char in spawn:
                            if target == target_char.name:
                                selected_target = target_char
                                dmg = attack(turn, selected_target)
                                break
                        if selected_target:
                            selected_target.stats["HP"] -= dmg
                            print(f"{turn.name} deals {dmg} damage to {selected_target.name}!\n")
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
            print("~~~\nSword of Belegost - 500 Gil ### Mithril Tipped Arrows - 300 Gil ### Mead - 100 Gil ### Tent - 200 Gil\n~~~")
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
            elif choice == "Tent" and gil >= 200:
                tents += 1
                gil -= 200

                        
                        
            elif choice == "Tent" and gil < 200:
                print("\nYou cant afford that!")
####################################################################  


            else:
                print(f"\nI don't have any {choice}!")
#########################END OF DWARF MERCHANT######################
        elif "elf" in merchant[0]:
            print("~~~\nJewel Crested Staff - 500 Gil ### Lembas - 120 Gil ### Ether - 200 Gil ### Tent - 200 Gil\n~~~")
            print(f"$$$ Current Gil: {gil} $$$\n")
            choice = input("Enter name of item or 'n' to quit and or return to previous menu: ")    
            if choice == "n" or choice == "N":
                return [party, gil, tents]
############# this logic encompuses one item!! #####################
            elif choice == "Jewel Crested Staff" and gil >= 500:
                target = input("Who will equip this? ")
                while True:
                    if target in partynames:
                        for mem in party:
                            if target == mem.name:
                                mem.stats["Int"] += 30
                                gil -= 500
                        break

                    elif target == "n" or target == "N":
                        break
                    else:
                        print("\nWho's that?")
                        break
                        
                        
            elif choice == "Jewel Crested Staff" and gil < 500:
                print("\nYou cant afford that!")
####################################################################          
######################################################################
            elif choice == "Lembas" and gil >= 120:
                target = input("Who will hold this? ")
                while True:
                    if target in partynames:
                        for mem in party:
                            if target == mem.name:
                                mem.inv.append("Lembas")
                                gil -= 120
                        break

                    elif target == "n" or target == "N":
                        break
                    else:
                        print("\nWho's that?")
                        break
                        
                        
            elif choice == "Lembas" and gil < 120:
                print("\nYou cant afford that!")
######################################################################
######################################################################
            elif choice == "Ether" and gil >= 200:
                target = input("Who will hold this? ")
                while True:
                    if target in partynames:
                        for mem in party:
                            if target == mem.name:
                                mem.inv.append("Ether")
                                gil -= 200
                        break

                    elif target == "n" or target == "N":
                        break
                    else:
                        print("\nWho's that?")
                        break
                        
                        
            elif choice == "Ether" and gil < 200:
                print("\nYou cant afford that!")
######################################################################
############# this logic encompuses TENT ! #####################
            elif choice == "Tent" and gil >= 200:
                tents += 1
                gil -= 200

                        
                        
            elif choice == "Tent" and gil < 200:
                print("\nYou cant afford that!")
####################################################################  
            else:
                print(f"\nI don't have any {choice}!")
#########################END OF ELF MERCHANT######################

        elif "hat" in merchant[0]:
            print("~~~\nMagic Mushrooms - 2000 Gil ### Old Toby - 2000 Gil\n~~~")
            print(f"$$$ Current Gil: {gil} $$$\n")
            choice = input("Enter name of item or 'n' to quit and or return to previous menu: ")    
            if choice == "n" or choice == "N":
                return [party, gil, tents]
############# this logic encompuses one item!! #####################
            elif choice == "Magic Mushrooms" and gil >= 2000:
                target = input("Who will use this? ")
                while True:
                    if target in partynames:
                        for mem in party:
                            if target == mem.name:
                                mem.stats["Luck"] += 30
                                gil -= 2000
                        break

                    elif target == "n" or target == "N":
                        break
                    else:
                        print("\nWho's that?")
                        break
                        
                        
            elif choice == "Magic Mushrooms" and gil < 2000:
                print("\nYou cant afford that!")
#################################################################### 
            elif choice == "Old Toby" and gil >= 2000:
                target = input("Who will use this? ")
                while True:
                    if target in partynames:
                        for mem in party:
                            if target == mem.name:
                                mem.stats["Eva"] += 30
                                gil -= 2000
                        break

                    elif target == "n" or target == "N":
                        break
                    else:
                        print("\nWho's that?")
                        break
                        
                        
            elif choice == "Old Toby" and gil < 2000:
                print("\nYou cant afford that!")
#################################################################### 
            else:
                print(f"\nI don't have any {choice}!")
#########################END OF TOM MERCHANT######################
    



def main():
    
    orc = jobs.Orc()
    wight = jobs.Wight()
    spider = jobs.Spider()
    chaosD = jobs.ChaosDwarf()
    chaosE = jobs.ChaosElf()
    easterling = jobs.Easterling()
    orcCap = jobs.OrcCap()
    watcher = jobs.Watcher()
    warg = jobs.Warg()
    

    
    
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
        
    print()
    if len(party) == 4:
        print(f"\n{party[0].name}, {party[1].name}, {party[2].name} and {party[3].name} set", end ="")
    elif len(party) == 3:
        print(f"\n{party[0].name}, {party[1].name}, and {party[2].name} set", end = "")
    elif len(party) == 2:
        print(f"\n{party[0].name} and {party[1].name} set", end="")
    else:
        print(f"\n{party[0].name} sets", end="")
    print(story.story2) 

    
    i = 0
    while i < 12:
        ##### This is one encounter #####
        enemies = [orc, spider, wight]
        loot = encounter(party, gil, enemies) #important to equate party, to update HP values etc   
        party = loot[0]
        gil = loot[1]
        for member in party:
            member.leveler(loot[2])   #change this multiplier to adjust xp rates but will not affect results screen
            member.statter()
            member.block = 0 #reset block states
            print(f"{member.name} is level {member.lvl} and has {member.xp} EXP")
    ##################################    
   
        print("\nYour party continues south...\n")
    
    ###########################
        party, gil, tents = shop(party, gil, tents)

        campsite(party, tents)
        i += 1
    

    enemies = [watcher]
    loot = encounter(party, gil, enemies) #important to equate party, to update HP values etc   
    party = loot[0]
    gil = loot[1]
    for member in party:
        member.leveler(loot[2])   #change this multiplier to adjust xp rates but will not affect results screen
        member.statter()
        member.block = 0 #reset block states
        print(f"{member.name} is level {member.lvl} and has {member.xp} EXP")
    ##################################  
  
    

    



main() 

