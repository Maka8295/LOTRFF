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

    "White Mage": ["Attack", "Block", "Cure"],

    "Black Mage": ["Attack", "Block", "Fire"],

    "Knight": ["Attack", "Block"],

    "Burglar": ["Attack", "Block", "Steal"],

}

 

class Character:

    def __init__(self, name):

        self.name = name

        self.stats = None

        self.job = None

        self.race = None

        self.skills = None

 

party = []

 

for i in range(4):

    character = Character(input("Enter name: "))

 

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

 

 

    if character.name == "Bilbo" or "Frodo" and character.race == "Hobbit":

        character.skills.append("Invisibility")

    if character.name == "Gandalf" and character.race == "Maia":

        character.skills.append("Fire of Anor")

    if character.name == "Gimli" and character.race == "Dwarf":

        character.skills.append("Toss me!")

    if character.name == "Cloud" and character.job == "Knight":

        character.skills.append("Omnislash")

    if character.name == "Legolas" and character.race == "Elf":

        character.skills.append("Double Strike")

    if character.name == "Aragorn" and character.race == "Man":

        character.skills.append("Blessings of Elrond")

 

   

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

 

 

print(vars(character.stats))

print(character.name)

print(character.job)

print(character.skills)

print(character.race)

 

while True:

    dmg = int(input("Enter DMG:\n"))

    vars(character.stats)["HP"] = int(vars(character.stats)["HP"]) - dmg

    print(f"Remaining HP: {vars(character.stats)['HP']}")

    if int(vars(character.stats)["HP"]) <= 0:

        print("You died!\n")
