import story
import jobs
import random as rd
import sys

def attack(user): #calculates damage based on user
    return user.stats["Str"] + rd.randint(-5,5)
def magic(user):
    return user.stats["Int"] + rd.randint(-5,5)


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
                return [party, gil_spawn, xp_spawn]
            if not active_party:
                sys.exit("Oh dear your party is dead!")  

            if turn in spawn:
                en_action = rd.choice(turn.skills)
                if en_action == "Block":
                    continue #to do
                if en_action == "Attack":
                    en_target = rd.choice(active_party)
                    en_dmg = attack(turn)
                    en_target.stats["HP"] -= en_dmg
                    print(f"{turn.name} uses {en_action} on {en_target.name} dealing {en_dmg} damage!\n")
                    if en_target.stats["HP"] <= 0:
                        active_party.remove(en_target)
                        print(f"{en_target.name} has been defeated!\n")

            elif turn in active_party:
                print("~~~")
                for member in party:
                    print(f"{member.name} - HP: {member.stats['HP']} - MP: {member.stats['MP']}")
                print("~~~\n")
                while True:
                    action = input(f"What will {turn.name} do?\n{turn.skills}\n\n")
                    if action in turn.skills:
                        break
                    print("\nInvalid selection!\n")
                
                if action == "Attack":
                    dmg = attack(turn)
                    while True:
                        target = input("Select Target:\n")  # if two orcs, first orc in turn order is targeted
                        selected_target = None
                        for target_char in spawn:
                            if target == target_char.name:
                                selected_target = target_char
                                break
                
                        if selected_target:
                            selected_target.stats["HP"] -= dmg
                            print(f"{turn.name} deals {dmg} damage to {selected_target.name}")
                            if selected_target.stats["HP"] <= 0:
                                spawn.remove(selected_target)
                            break
                        else:
                            print("Invalid target!\n")               



















def main():
    party = []
    gil = 0

    print(story.story1)

    for _ in range(4): 
        name = input("What is the name of this character? ")
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

    loot = encounter(party) #important to equate party, to update HP values etc   
    party = loot[0]
    gil += loot[1]
    for member in party:
        member.leveler(loot[2])
        print(member.lvl, member.xp)

    print(gil)
    




main() 

