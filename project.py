import story
import jobs
from jobs import Levels
from jobs import WhiteMage
from jobs import BlackMage
from jobs import Knight
from jobs import Burglar
from jobs import Bard
import random as rd
import sys


def attack(user, target):  # calculates damage based on user
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
                dmg = user.stats["Str"] + rd.randint(-5, 5) - dmg_reduction
            else:
                dmg = user.stats["Str"] * 2 + rd.randint(-20, 20) - dmg_reduction
        else:
            dmg = (user.stats["Str"] + rd.randint(-5, 5) - dmg_reduction) / 2
        if dmg < 0:
            return 0
        else:
            return dmg
    else:
        return 0


def magic(user, target):  # calculates damage based on user
    ev_rate = target.stats["Eva"] / 100
    crit_rate = user.stats["Luck"] / 100
    crit = False
    roll = rd.random()
    crit_roll = rd.random()
    if crit_roll < crit_rate:
        crit = True
    if roll > ev_rate:
        dmg_reduction = target.stats["Spi"] / 2
        if target.block == False:
            if crit == False:
                dmg = user.stats["Int"] + rd.randint(-5, 5) - dmg_reduction
            else:
                dmg = user.stats["Int"] * 2 + rd.randint(-20, 20) - dmg_reduction
        else:
            dmg = (user.stats["Int"] + rd.randint(-5, 5) - dmg_reduction) / 2
        if dmg < 0:
            return 0
        else:
            return dmg
    else:
        return 0


def cure(user):  # calculates damage based on user
    crit_rate = user.stats["Luck"] / 100
    crit = False
    crit_roll = rd.random()
    if crit_roll < crit_rate:
        crit = True
    if crit == False:
        dmg = user.stats["Int"] + rd.randint(-5, 5)
    else:
        dmg = user.stats["Int"] * 2 + rd.randint(-20, 20)
    return dmg


def campsite(party, tents):
    print(story.campsitestory)
    print(f"\nNumber of tents: {tents}\n")
    ans = input()
    if ans == "n" or ans == "N":
        return party, tents
    else:
        return rest(party, tents)


def rest(party, tents):  # returns healed party and tents - 1
    for member in party:
        member.stats["HP"] = member.stats["HPMax"]
        member.stats["MP"] = member.stats["MPMax"]
    tents -= 1
    return party, tents


def turn_orderer(
    turn_order,
):  # takes in raw turn order, then sorts according to speed and returns
    return sorted(
        turn_order, key=lambda character: character.stats["Spd"], reverse=True
    )


def encounter(party, gil, enemies):  # return [party, new gill amt, xp gained]
    orc = jobs.Orc()
    wight = jobs.Wight()
    spider = jobs.Spider()
    chaosD = jobs.ChaosDwarf()
    chaosE = jobs.ChaosElf()
    easterling = jobs.Easterling()
    orcCap = jobs.OrcCap()
    watcher = jobs.Watcher()
    warg = jobs.Warg()

    enemy_no = rd.randint(1, 4)
    spawn = []
    turn_order = []
    for i in range(enemy_no):
        spawn.append(rd.choice(enemies))
    for mob in spawn:
        if mob.name == "Watcher":
            spawn = [watcher]
        if mob.name == "Orc Captain":
            spawn = [warg, warg, orcCap]

    gil_spawn = len(spawn) * 100 + rd.randint(-20, 20)
    gil += gil_spawn
    xp_spawn = len(spawn) * 50 + rd.randint(-20, 20)

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
                print(
                    "###############################ENCOUNTER END#############################\n"
                )
                print(
                    f"You recieve {gil_spawn} gil and each member of your party recieves {xp_spawn} EXP!\n"
                )
                return [party, gil, xp_spawn]
            if not active_party:
                sys.exit("Oh dear your party is dead!")

            if turn in spawn:
                turn.block = False
                en_action = rd.choice(turn.skills)
                if en_action == "Block":
                    turn.block = True  # to do
                    print(f"{turn.name} blocks!\n")

                if en_action == "Attack":
                    en_target = rd.choice(active_party)
                    en_dmg = attack(turn, en_target)
                    en_target.stats["HP"] -= en_dmg
                    print(
                        f"{turn.name} uses {en_action} on {en_target.name} dealing {en_dmg} damage!\n"
                    )
                    if en_target.stats["HP"] <= 0:
                        en_target.stats["HP"] = 0
                        active_party.remove(en_target)
                        print(f"{en_target.name} has been defeated!\n")

            elif turn in active_party and turn.stats["HP"] > 0:
                print("**************************ENEMIES***************************")
                for _ in spawn:
                    print(_.name, " ", end="")
                print(
                    "\n**************************ENEMIES***************************\n"
                )

                block = False
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~PARTY~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                for member in party:
                    print(
                        f"{member.name} - HP: {member.stats['HP']} - MP: {member.stats['MP']}"
                    )
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
                                        print(
                                            f"\n{turn.name} uses Lembas on {lembas_target} healing 100 HP!"
                                        )
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
                                        print(
                                            f"\n{turn.name} uses an Ether on {ether_target} restoring 100 MP!"
                                        )
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
                                        print(
                                            f"\n{turn.name} uses Mead on {mead_target} healing 60 HP!"
                                        )
                                        used_item = True
                                        break

                        elif selection == "n" or selection == "N":
                            break
                        else:
                            print("That item doesn't exist!\n")

                if action == "Fire":
                    while True:
                        target = input(
                            "Select Target: "
                        )  # if two orcs, first orc in turn order is targeted
                        selected_target = None
                        for target_char in spawn:
                            if target == target_char.name:
                                selected_target = target_char
                                dmg = magic(turn, selected_target)
                                break
                        if (
                            selected_target
                            and target in ["Wight", "Warg"]
                            and turn.stats["MP"] >= 20
                        ):
                            turn.stats["MP"] -= 10
                            selected_target.stats["HP"] -= dmg * 2
                            print(
                                f"{turn.name} deals {dmg * 2} fire damage to {selected_target.name}!\nIt's super effective!\n"
                            )
                            if selected_target.stats["HP"] <= 0:
                                selected_target.stats["HP"] = 0
                                spawn.remove(selected_target)
                            break
                        elif selected_target and turn.stats["MP"] >= 20:
                            turn.stats["MP"] -= 10
                            selected_target.stats["HP"] -= dmg
                            print(
                                f"{turn.name} deals {dmg} fire damage to {selected_target.name}!\n"
                            )
                            if selected_target.stats["HP"] <= 0:
                                selected_target.stats["HP"] = 0
                                spawn.remove(selected_target)
                            break
                        else:
                            if turn.stats["MP"] < 20:
                                print("Not enough MP!\n")
                                break
                            print("Invalid target!\n")

                if action == "Ice":
                    while True:
                        target = input(
                            "Select Target: "
                        )  # if two orcs, first orc in turn order is targeted
                        selected_target = None
                        for target_char in spawn:
                            if target == target_char.name:
                                selected_target = target_char
                                dmg = magic(turn, selected_target)
                                break
                        if (
                            selected_target
                            and target in ["Easterling", "Spider"]
                            and turn.stats["MP"] >= 20
                        ):
                            turn.stats["MP"] -= 10
                            selected_target.stats["HP"] -= dmg * 2
                            print(
                                f"{turn.name} deals {dmg * 2} ice damage to {selected_target.name}!\nIt's super effective!\n"
                            )
                            if selected_target.stats["HP"] <= 0:
                                selected_target.stats["HP"] = 0
                                spawn.remove(selected_target)
                            break
                        elif selected_target and turn.stats["MP"] >= 20:
                            turn.stats["MP"] -= 10
                            selected_target.stats["HP"] -= dmg
                            print(
                                f"{turn.name} deals {dmg} ice damage to {selected_target.name}!\n"
                            )
                            if selected_target.stats["HP"] <= 0:
                                selected_target.stats["HP"] = 0
                                spawn.remove(selected_target)
                            break
                        else:
                            if turn.stats["MP"] < 20:
                                print("Not enough MP!\n")
                                break
                            print("Invalid target!\n")

                if action == "Lightning":
                    if spawn and turn.stats["MP"] >= 50:
                        turn.stats["MP"] -= 50
                        for mob in spawn:
                            dmg = magic(turn, mob)
                            mob.stats["HP"] -= dmg
                            if mob.stats["HP"] <= 0:
                                spawn.remove(mob)
                            print(
                                f"{turn.name} deals {dmg} lightning damage to {mob.name}!\n"
                            )

                    elif "Watcher" in spawn and turn.stats["MP"] >= 50:
                        dmg = magic(turn, watcher)
                        turn.stats["MP"] -= 50
                        watcher.stats["HP"] -= dmg * 2
                        print(
                            f"{turn.name} deals {dmg * 2} lightning damage to {selected_target.name}!\nIt's super effective!\n"
                        )
                        if watcher.stats["HP"] <= 0:
                            watcher.stats["HP"] = 0
                            spawn.remove(watcher)
                        break
                    else:
                        if turn.stats["MP"] < 50:
                            print("Not enough MP!\n")
                            break

                if action == "Song":
                    if turn.stats["MP"] >= 5:
                        songheal = turn.stats["Int"] + rd.randint(-5, 5)
                        turn.stats["MP"] -= 5
                        for mem in active_party:
                            if mem.stats["HP"] + songheal >= mem.stats["HPMax"]:
                                mem.stats["HP"] = mem.stats["HPMax"]
                            else:
                                mem.stats["HP"] += songheal
                        print(
                            f"{turn.name} sings a song, the party is healed by {songheal} HP!\n"
                        )
                    else:
                        print("Not enough MP!\n")
                if action == "Steal":
                    steal_target = rd.choice(spawn)
                    steal_gil = rd.randint(0, turn.stats["Spd"] * 10)
                    gil += steal_gil
                    print(
                        f"{turn.name} steals {steal_gil} Gil from {steal_target.name}!\n"
                    )

                if action == "Holy":
                    while True:
                        target = input("Select Target: ")
                        selected_target = None
                        for target_char in spawn:
                            if (
                                target == "Wight"
                                or target == "Chaos Elf"
                                or target == "Chaos Dwarf"
                            ) and target_char.name == target:
                                selected_target = target_char
                                break
                        if selected_target and turn.stats["MP"] >= 30:
                            turn.stats["MP"] -= 30
                            spawn.remove(selected_target)
                            print(f"{turn.name} smites {selected_target.name}!\n")
                            break
                        else:
                            if turn.stats["MP"] < 20:
                                print("Not enough MP!\n")
                                break
                            print("Invalid target!\n")
                            break

                if action == "Attack":
                    while True:
                        target = input(
                            "Select Target: "
                        )  # if two orcs, first orc in turn order is targeted
                        selected_target = None
                        for target_char in spawn:
                            if target == target_char.name:
                                selected_target = target_char
                                dmg = attack(turn, selected_target)
                                break
                        if selected_target:
                            selected_target.stats["HP"] -= dmg
                            print(
                                f"{turn.name} deals {dmg} damage to {selected_target.name}!\n"
                            )
                            if selected_target.stats["HP"] <= 0:
                                selected_target.stats["HP"] = 0
                                spawn.remove(selected_target)
                            break
                        else:
                            print("Invalid target!\n")

                if action == "Cure":
                    while True:
                        target = input(
                            "Select Target: "
                        )  # if two orcs, first orc in turn order is targeted
                        selected_target = None
                        for target_char in active_party:
                            if target == target_char.name:
                                selected_target = target_char
                                dmg = cure(turn)
                                break
                        if selected_target and turn.stats["MP"] >= 20:
                            turn.stats["MP"] -= 20
                            selected_target.stats["HP"] += dmg
                            print(
                                f"{turn.name} heals {selected_target.name} by {dmg}!\n"
                            )
                            if (
                                selected_target.stats["HP"]
                                > selected_target.stats["HPMax"]
                            ):
                                selected_target.stats["HP"] = selected_target.stats[
                                    "HPMax"
                                ]
                            break
                        else:
                            if turn.stats["MP"] < 20:
                                print("Not enough MP!\n")
                                break
                            print("Invalid target!\n")


def shop(party, gil, tents):  # returns list with [party, gil, tents]
    merchant = story.dynamicstory()
    print(f"{merchant[0]}\n")
    print("What will it be then?\n")
    partynames = []
    for mem in party:
        partynames.append(mem.name)
    while True:
        if "dwarf" in merchant[0]:
            print(
                "~~~\nSword Upgrade - Knights - 500 Gil ### Bow and Dagger Upgrade - Bards, Burglars - 300 Gil ### Mead - HP - 100 Gil ### Tent - 200 Gil\n~~~"
            )
            print(f"$$$ Current Gil: {gil} $$$\n")
            choice = input(
                "Enter 1,2,3 or 4 for corresponding item or 'n' to quit and or return to previous menu: "
            )
            if choice == "n" or choice == "N":
                return [party, gil, tents]
            ############# this logic encompuses one item!! #####################
            elif choice == "1" and gil >= 500:
                target = input("Who will equip this? ")
                while True:
                    if target in partynames:
                        found = False
                        for mem in party:
                            if target == mem.name and isinstance(mem, Knight):
                                mem.stats["Str"] += 30
                                gil -= 500
                                found = True
                        if found == False:
                            print(f"\n{target} can't use that!")
                        break

                    elif target == "n" or target == "N":
                        break

                    else:
                        print("\nWho's that?")
                        break

            elif choice == "1" and gil < 500:
                print("\nYou cant afford that!")
            ####################################################################
            elif choice == "2" and gil >= 300:
                target = input("Who will equip this? ")
                while True:
                    if target in partynames:
                        found = False
                        for mem in party:
                            if target == mem.name and (
                                isinstance(mem, Bard) or isinstance(mem, Burglar)
                            ):
                                mem.stats["Str"] += 20
                                gil -= 300
                                found = True
                        if found == False:
                            print(f"\n{target} can't use that!")
                        break

                    elif target == "n" or target == "N":
                        break
                    else:
                        print("\nWho's that?")
                        break

            elif choice == "2" and gil < 300:
                print("\nYou cant afford that!")
            ######################################################################
            elif choice == "3" and gil >= 100:
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

            elif choice == "3" and gil < 100:
                print("\nYou cant afford that!")
            ######################################################################
            ############# this logic encompuses TENT ! #####################
            elif choice == "4" and gil >= 200:
                tents += 1
                gil -= 200

            elif choice == "4" and gil < 200:
                print("\nYou cant afford that!")
            ####################################################################

            else:
                print(f"\nI don't have any {choice}!")
        #########################END OF DWARF MERCHANT######################
        elif "elf" in merchant[0]:
            print(
                "~~~\nStaff Upgrade - White Mage, Black Mage - 500 Gil ### Lembas - HP - 120 Gil ### Ether - MP - 200 Gil ### Tent - 200 Gil\n~~~"
            )
            print(f"$$$ Current Gil: {gil} $$$\n")
            choice = input(
                "Enter 1,2,3 or 4 for corresponding item or 'n' to quit and or return to previous menu: "
            )
            if choice == "n" or choice == "N":
                return [party, gil, tents]
            ############# this logic encompuses one item!! #####################
            elif choice == "1" and gil >= 500:
                target = input("Who will equip this? ")
                while True:
                    if target in partynames:
                        found = False
                        for mem in party:
                            if target == mem.name and (
                                isinstance(mem, WhiteMage) or isinstance(mem, BlackMage)
                            ):
                                mem.stats["Int"] += 30
                                gil -= 500
                                found = True
                        if found == False:
                            print(f"\n{target} can't use that!")
                        break

                    elif target == "n" or target == "N":
                        break
                    else:
                        print("\nWho's that?")
                        break

            elif choice == "1" and gil < 500:
                print("\nYou cant afford that!")
            ####################################################################
            ######################################################################
            elif choice == "2" and gil >= 120:
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

            elif choice == "2" and gil < 120:
                print("\nYou cant afford that!")
            ######################################################################
            ######################################################################
            elif choice == "3" and gil >= 200:
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

            elif choice == "3" and gil < 200:
                print("\nYou cant afford that!")
            ######################################################################
            ############# this logic encompuses TENT ! #####################
            elif choice == "4" and gil >= 200:
                tents += 1
                gil -= 200

            elif choice == "4" and gil < 200:
                print("\nYou cant afford that!")
            ####################################################################
            else:
                print(f"\nI don't have any {choice}!")
        #########################END OF ELF MERCHANT######################

        elif "hat" in merchant[0]:
            print(
                "~~~\nMagic Mushrooms - ??? - 2000 Gil ### Old Toby - ??? - 2000 Gil\n~~~"
            )
            print(f"$$$ Current Gil: {gil} $$$\n")
            choice = input(
                "Enter 1 or 2 for corresponding item or 'n' to quit and or return to previous menu: "
            )
            if choice == "n" or choice == "N":
                return [party, gil, tents]
            ############# this logic encompuses one item!! #####################
            elif choice == "1" and gil >= 2000:
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

            elif choice == "1" and gil < 2000:
                print("\nYou cant afford that!")
            ####################################################################
            elif choice == "2" and gil >= 2000:
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

            elif choice == "2" and gil < 2000:
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
    multi = 1
    if len(sys.argv) > 1 and sys.argv[1] == "moneybags":
        gil = 9999
    if len(sys.argv) > 1 and sys.argv[1] == "journalistmode":
        multi = 10
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

        ##########################################Hidden Characters Logic########
        if char.name == ("Gandalf" or "gandalf") and char.race == "Maia":
            if "Fire" not in char.skills:
                char.skills.append("Fire")
            if "Cure" not in char.skills:
                char.skills.append("Cure")
            char.stats = {
                "HP": 200,
                "HPMax": 200,
                "MP": 200,
                "MPMax": 200,
                "Str": 150,
                "Int": 300,
                "Def": 100,
                "Spi": 100,
                "Spd": 35,
                "Eva": 20,
                "Luck": 20,
            }
            print(f"\nHidden character {char.name} found!")

        if (
            char.name == ("Frodo" or "Bilbo" or "frodo" or "bilbo")
            and char.race == "Hobbit"
        ):
            char.stats = {
                "HP": 70,
                "HPMax": 70,
                "MP": 100,
                "MPMax": 100,
                "Str": 40,
                "Int": 40,
                "Def": 50,
                "Spi": 50,
                "Spd": 50,
                "Eva": 60,
                "Luck": 60,
            }
            print(f"\nHidden character {char.name} found!")

        if char.name == ("Gimli" or "gimli") and char.race == "Dwarf":
            char.stats = {
                "HP": 250,
                "HPMax": 250,
                "MP": 20,
                "MPMax": 20,
                "Str": 200,
                "Int": 20,
                "Def": 150,
                "Spi": 80,
                "Spd": 10,
                "Eva": 10,
                "Luck": 10,
            }
            print(f"\nHidden character {char.name} found!")

        if char.name == ("Legolas" or "legolas") and char.race == "Elf":
            char.stats = {
                "HP": 150,
                "HPMax": 150,
                "MP": 150,
                "MPMax": 150,
                "Str": 150,
                "Int": 150,
                "Def": 100,
                "Spi": 100,
                "Spd": 50,
                "Eva": 50,
                "Luck": 10,
            }
            print(f"\nHidden character {char.name} found!")

        if char.name == ("Aragorn" or "aragorn") and char.race == "Man":
            char.stats = {
                "HP": 220,
                "HPMax": 220,
                "MP": 150,
                "MPMax": 150,
                "Str": 180,
                "Int": 180,
                "Def": 180,
                "Spi": 180,
                "Spd": 35,
                "Eva": 20,
                "Luck": 20,
            }
            print(f"\nHidden character {char.name} found!")

        if (
            char.name == ("Vivi" or "vivi")
            and char.race == "Hobbit"
            and isinstance(char, BlackMage)
        ):
            char.skills.append("Holy")
            char.stats = {
                "HP": 9999,
                "HPMax": 9999,
                "MP": 9999,
                "MPMax": 9999,
                "Str": 999,
                "Int": 999,
                "Def": 999,
                "Spi": 999,
                "Spd": 999,
                "Eva": 100,
                "Luck": 100,
            }
            print(f"\nUltra hidden character {char.name} found!!!")
        ##########################################
        party.append(char)
        print("\n~~~ Current Party Members ~~~")
        for person in party:
            print(f"{person.name}  ", end="")

        if len(party) == 4:
            break
        ans = input("\n\nWould you like to make another character? Y/n\n")
        if ans == "n" or ans == "N":
            break

    print()
    if len(party) == 4:
        print(
            f"\n{party[0].name}, {party[1].name}, {party[2].name} and {party[3].name} set",
            end="",
        )
    elif len(party) == 3:
        print(f"\n{party[0].name}, {party[1].name}, and {party[2].name} set", end="")
    elif len(party) == 2:
        print(f"\n{party[0].name} and {party[1].name} set", end="")
    else:
        print(f"\n{party[0].name} sets", end="")
    print(story.story2)

    i = 0
    while i <= 16:
        choice = rd.choice([1, 2, 3, 4])
        if choice == 1 or choice == 2:
            party, gil = encounterfull(
                party, gil, [orc, spider, wight, warg, easterling, chaosE, chaosD]
            )
        elif choice == 3:
            party, gil, tents = shop(party, gil, tents)
        elif choice == 4:
            party, tents = campsite(party, tents)
        if i == 15:
            print(story.story3)
            party, gil = encounterfull(party, gil, [orcCap])
        if i == 16:
            print(story.story4)
            party, gil = encounterfull(party, gil, [watcher])
            print(story.story5)
            sys.exit("Congratulations! You have beaten the game!")
        i += 1


def encounterfull(party, gil, enemies):
    loot = encounter(
        party, gil, enemies
    )  # important to equate party, to update HP values etc
    party = loot[0]
    gil = loot[1]
    for member in party:
        member.leveler(
            loot[2]
        )  # change this multiplier to adjust xp rates but will not affect results screen
        member.statter()
        member.block = 0  # reset block states
        print(f"{member.name} is level {member.lvl} and has {member.xp} EXP")
    print("\nYour party continues south...\n")
    return party, gil


if __name__ == "__main__":
    main()
