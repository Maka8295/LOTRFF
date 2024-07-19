import random as rd

story1 = "Elrond, Lord of Imladris has entrusted your party with a dangerous quest.\nYou are to investigate reports of strange sightings at the base of the mountains of Celebdil.\nWho is departing on this quest?\n"

story2 = " out from Imladris, horses laden with lembas and supplies have been gifted to the party from Lord Elrond.\nThe party makes south, following the edge of the Misty Mountains.\n"

campsitestory = "\nThe party finds a nook in the eastern rockface suitable for setting up a camp.\nDoes the party use a tent and rest? Y/n "

def dynamicstory():
    
    
    dwarf = "The party encounters a rugged dwarf walking towards them bearing a large pack. \nHe introduces himself as a travelling merchant from the Blue Mountains. \nHe offers the party a variety of weapons and items."

    elf = "A jovial elf meanders towards the party from a clearing in the forest to their right.\nHe introduces himself as a traveler from the Grey Havens.\nA white horse trails behind him with a trailer of goods."

    tom = "The party notices a tall blue hat bobbing up and down in a patch of tall grass in front of them.\nThe strange man, albeit friendly refuses to make his name known.\nHe offers the party a variety of items he has collected."
    weights = [0.4, 0.4, 0.2]
    return rd.choices([dwarf, elf, tom], weights=weights, k=1) #returns a list

story3 = "An Orc Captain assails the party as they near their destination!"

story4 = "The party reaches a large body of water near the base of the mountain.\nThere is evidence that many dwarves fled from the surrounding mines and into the wilderland.\nThe surface of the water begins to bubble...\n"

story5 = "The Watcher of the lake has been defeated, and peace restored to Khazad-Dum. The Elves and Dwarves corrupted by its strange magic have been cured... for now..."
