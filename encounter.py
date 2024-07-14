import jobs
import random as rd
def encounter():
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
    
    turn_order.extend(party)
    turn_order.extend(spawn)

    turn_order = sorted(turn_order, key =lambda character: char.stats.Speed, reverse=True)
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
