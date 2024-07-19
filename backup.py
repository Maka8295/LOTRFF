    i = 0
    while i < 12:
        ##### This is one encounter #####
        enemies = [orc, spider, wight, warg, easterling, chaosE, chaosD]
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
        ##################################

        print("\nYour party continues south...\n")

        ###########################
        party, gil, tents = shop(party, gil, tents)

        campsite(party, tents)
        i += 1


    print(story.story3)
    

    enemies = [orcCap]
    loot = encounter(
        party, gil, enemies
    )  # important to equate party, to update HP values etc
    party = loot[0]
    gil = loot[1]
    for member in party:
        member.leveler(
            loot[2] * multi
        )  # change this multiplier to adjust xp rates but will not affect results screen
        member.statter()
        member.block = 0  # reset block states
        print(f"{member.name} is level {member.lvl} and has {member.xp} EXP")

    
    print(story.story4)
    

    enemies = [watcher]
    loot = encounter(
        party, gil, enemies
    )  # important to equate party, to update HP values etc
    party = loot[0]
    gil = loot[1]
    for member in party:
        member.leveler(
            loot[2] * multi
        )  # change this multiplier to adjust xp rates but will not affect results screen
        member.statter()
        member.block = 0  # reset block states
        print(f"{member.name} is level {member.lvl} and has {member.xp} EXP")
