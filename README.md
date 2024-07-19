# LOTRFF
My final project for CS50P, a text-based turn-based RPG set in Middle Earth with Final Fantasy themes (because I am very original). Focus has been put on coding the working parts rather than balance, so it may be too easy, random, or too hard in parts!

Features:

Ability to make a party of up to 4 characters each with a race, job and name. Job will affect your characters stats and abilities. Hidden abilities and stat boosts exist for certain combinations of names, races and jobs!

Turn based combat with healing / buff items, physical and magical attacks, and blocking. Enemies will drop gil.

Levelling up system in which XP earned from encounters will level up your characters and increase their stats.

Ability to rest at campsites to restore HP and MP.

Skills:

Attack - Deal physical damage based with characters strength against targets defense, can critical depending on luck, and will miss depending on evasion.

Block - Reduces incoming damage by roughly half until next turn

Item - Use any item held in inventory, each character has a seperate inventory

Song - Heal all members in active party by an ammount based on characters inteligence, costs 5 MP

Holy - Instantly kills any undead monster

Cure - Heals HP of target party member by large ammount, based on characters inteligence, costs 20 MP

Steal - Steals gil from enemies based on users speed.

Fire and Ice - Deal magic based damage with characters Inteligence against targets spirit, costs 20 MP. Different monsters are weak and resistant to some attacks!

Lightning - Same as above except is an AOE attack that costs 50 MP.

Items: Lembas - Heals 100 HP, Mead - Heals 60 HP.

Secret items are available from Tom to increase evasion and luck stats!

You can pass an argument after "python game.py ????" to enable cheats for increased Gil or EXP!

How to install:

Clone this repository then execute game.py

How to play:

Enter names exactly how they appear on screen, for example if prompted for a target, to target an enemy Orc, you must input exactly "Orc".

Some menus can be navigated with Y/N, the capital letter is the default, so you can just push enter to proceed, if you want to select "No" or back, type "n" or "N".


