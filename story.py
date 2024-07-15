import random as rd

story1 = "Elrond, Lord of Imladris has entrusted your party with a dangerous quest.\nYou are to investigate reports of strange sightings at the base of the mountains of Celebdil.\nWho is departing on this quest?\n"

story2 = " out from Imladris, horses laden with lembas and supplies have been gifted to the party from Lord Elrond.\nThe party makes south, following the edge of the Misty Mountains.\n"

campsitestory = "\nThe party finds a nook in the eastern rockface suitable for setting up a camp.\nDoes the party use a test and rest? Y/n "

def dynamicstory():
    
    
    dwarf = "The party encounters a rugged dwarf walking towards them bearing a large pack. \nHe introduces himself as a travelling merchant from the Blue Mountains. \nHe offers the party a variety of weapons and items."

    elf = "A jovial elf meanders towards the party from a clearing in the forest to their right.\nHe introduces himself as a traveler from the Grey Havens.\nA white horse trails behind him with a trailer of goods."

    tom = "The party notices a tall blue hat bobbing up and down in a patch of tall grass in front of them.\nThe strange man, albeit friendly refuses to make his name known.\nHe offers the party a variety of items he has collected."
    weights = [1, 0, 0]
    return rd.choices([dwarf, elf, tom], weights=weights, k=1) #returns a list
