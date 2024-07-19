# LOTRFF
My final project for CS50P, a text-based turn-based RPG set in Middle Earth with Final Fantasy themes (because I am very original). Focus has been put on coding the working parts rather than balance, so it may be too easy, random, or too hard in parts!

#### Video Demo:  https://www.youtube.com/watch?v=y0XCcQgORzM

## How it works

My project has three main files, jobs.py which contains the classes for each job that you can use in the character creator as well as the stats of the enemies. I use class methods to handle the levelling and increase of stats for the party members. Your skills and items for each character are also held within each class.

project.py is the main file for the game, which defines the logic for the combat system, shops, character creation etc. The number of tents and gill are also stored here. The way the game works is by passing a list, containing each of your party members (class objects) into certain functions, such as an encounter function, once the encounter ends the function returns your party list with updated EXP, values, items, Gil and so on. It's also possible to pass in certain enemies to the encounter function, so I can have some control over what the party encounters rather than being completely random.

Finally is story.py which contains a tiny bit of logic for randomizing the 3 different merchants you can encounter, but mainly just text for the story.

## Features

- Ability to make a party of up to 4 characters each with a race, job and name. Job will affect your characters stats and abilities. Hidden abilities and stat boosts exist for certain combinations of names, races and jobs!

- Turn based combat with healing / buff items, physical and magical attacks, and blocking. Enemies will drop gil.

- Levelling up system in which XP earned from encounters will level up your characters and increase their stats.

- Ability to rest at campsites to restore HP and MP.

- You can pass an argument after "project.py" to enable cheats for increased Gil or EXP!

- Shop from merchants to buy healing items, weapon upgrades and tents.

## Skills

- Attack - Deal physical damage based with characters strength against targets defense, can critical depending on luck, and will miss depending on evasion.

- Block - Reduces incoming damage by roughly half until next turn

- Item - Use any item held in inventory, each character has a seperate inventory

- Song - Heal all members in active party by an ammount based on characters inteligence, costs 5 MP

- Holy - Instantly kills any undead monster

- Cure - Heals HP of target party member by large ammount, based on characters inteligence, costs 20 MP

- Steal - Steals gil from enemies based on users speed.

- Fire and Ice - Deal magic based damage with characters Inteligence against targets spirit, costs 20 MP. Different monsters are weak and resistant to some attacks!

- Lightning - Same as above except is an AOE attack that costs 50 MP.

- Items: Lembas - Heals 100 HP, Mead - Heals 60 HP, Ether - Heals 100 MP.

- Secret items are available from Tom to increase evasion and luck stats!


## How to install

You must have Python installed to play the game!

Clone this repository by pasting the following into your terminal:

```
git clone https://github.com/Maka8295/LOTRFF.git
```
Or you can download simply download (or copy and paste) the project.py file, jobs.py file and the story.py file, make sure they are all in the same directory!

## How to play

Move to the directory that you cloned the repository or downloaded the files and run the following in your terminal.
```
cd path/to/your/directory
```

```
python project.py
```
Optionally enter the secret codes after project.py for cheats! (You will have to find them in the source code!)

Enter names exactly how they appear on screen, for example if prompted for a target, to target an enemy Orc, you must input exactly "Orc".

Some menus can be navigated with Y/N, the capital letter is the default, so you can just push enter to proceed, if you want to select "No" or back, type "n" or "N".


