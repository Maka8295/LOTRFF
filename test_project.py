import pytest
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
from project import attack
from project import magic
from project import cure
from project import campsite
from project import rest
from project import turn_orderer
from project import encounter
from project import shop
from project import encounterfull

wm = WhiteMage("white", "Maia")
bm = BlackMage("black", "Elf")
kn = Knight("knight", "Dwarf")
bg = Burglar("burglar", "Hobbit")

orc = jobs.Orc()

def test_attack():
    party = [wm, bm, kn, bg]
    party[2].stats["Eva"] = 100
    assert attack(orc, party[2]) == 0
    orc.stats["Eva"] = 0
    assert attack(party[2], orc) != 0

def test_magic():
    party = [wm, bm, kn, bg]
    orc.stats["Eva"] = 0
    assert (party[1], orc) != 0

def test_cure():
    party = [wm, bm, kn, bg]
    party[0].stats["HP"] = 1
    party[0].stats["HP"] += cure(party[0])
    assert party[0].stats["HP"] > 1

def test_rest():
    party = [wm, bm, kn, bg]
    tents = 1
    for member in party:
        member.stats["HP"] = 1
        member.stats["MP"] = 1
    party, tents = rest(party, tents)
    assert tents == 0
    assert party[0].stats["HP"] == party[0].stats["HPMax"]
    assert party[1].stats["HP"] == party[1].stats["HPMax"]
    assert party[2].stats["HP"] == party[2].stats["HPMax"]
    assert party[3].stats["HP"] == party[3].stats["HPMax"]

    assert party[0].stats["MP"] == party[0].stats["MPMax"]
    assert party[1].stats["MP"] == party[1].stats["MPMax"]
    assert party[2].stats["MP"] == party[2].stats["MPMax"]
    assert party[3].stats["MP"] == party[3].stats["MPMax"] 

def test_turn_orderer():
    turn_order = [wm, bm, kn, bg, orc]
    turn_order[0].stats["Spd"] = 1
    turn_order[1].stats["Spd"] = 2
    turn_order[2].stats["Spd"] = 3
    turn_order[3].stats["Spd"] = 4
    turn_order[4].stats["Spd"] = 5

    assert turn_orderer(turn_order) == [orc, bg, kn, bm, wm]
