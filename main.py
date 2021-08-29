# This is a sample Python script.

import MONSTER
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


MONSTERLIST = [MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER()]

MONSTERLIST[0].MONSTER("Orc","Forest",1,14,15)
MONSTERLIST[1].MONSTER("Ankheg","Forest",2,39,14)
MONSTERLIST[2].MONSTER("Orc Chief","Forest",3,35,16)
MONSTERLIST[3].MONSTER("BugBear","Forest",1,27,16)
MONSTERLIST[4].MONSTER("BugBear Chief","Forest",3,65,17)
MONSTERLIST[5].MONSTER("Chasme","Night Forest",6,84,15)
MONSTERLIST[6].MONSTER("Dretch","Night Forest",.25,18,11)
MONSTERLIST[7].MONSTER("Displacer Beast","Night",3,85,13)
MONSTERLIST[8].MONSTER("Farie Dragon ","Forest",2,14,15)
MONSTERLIST[9].MONSTER("Hook Horror","Night",3,75,15)
MONSTERLIST[10].MONSTER("Owl Bear","Forest",3,59,13)
MONSTERLIST[11].MONSTER("Thri-Kreen","Plains",1,30,15)


def RatingPicking():
    userInput = input("what challange rating do you want\n")
    monList = []
    for x in MONSTERLIST:
        if x.chalangeRating == int(userInput):
            monList.append(x)
    return monList

def TerrainPicking():
    userInput = input("what terrain do you want\n")
    monList = []
    for x in MONSTERLIST:
        if x.terrain == userInput:
            monList.append(x)
    return monList

def DifficultyPicking():
    userInput = input("what Difficulty do you want\n")
    monList=[]
    for x in MONSTERLIST:
        if x.chalangeRating == userInput:
            monList.append(x)
    return monList

def PickEncounter(choice):
    choiceDiction = {"rating": (lambda : RatingPicking()),
                      "terrain":lambda :TerrainPicking(),
                       "difficulty":lambda :DifficultyPicking()}
    CurrentMonsterList = choiceDiction.get(choice)
    return CurrentMonsterList()





def main():

    print("how would you like to pick? by chanange rating, terrain, or Difficulty")
    userput = input("")
    print(userput)
    x = PickEncounter(userput)
    for mon in x:
        print(mon.name)

main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/