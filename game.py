import story
import jobs


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
        
        ans = input("\n\nWould you like to make another character? Y/n\n")
        if ans == "n" or ans == "N":
            break
        
    



    print(party[0].name, party[0].race, party[0].xp, party[0].lvl)
    party[0].leveler(10000)
    print(party[0].xp, party[0].lvl)
main() 

