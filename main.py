# This is a sample Python script.

import MONSTER
import math
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

CHALLANGETOEXPDIC = {.25:50,.5:100,1:200,2:450,3:700,4:1100,5:1800,6:2300,7:2900,8:3900,9:5000,10:5900,11:7200,12:8400,13:10000,14:11500,15:13000,16:15000,17:18000,18:20000,19:22000,20:25000,21:33000,22:41000,23:50000,
24:62000,30:155000}

totalExpGain = 0

MONSTERLIST = [MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER(),
               MONSTER.MONSTER(),MONSTER.MONSTER()]


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
MONSTERLIST[12].MONSTER("Aarakocra","Everywhere",.25,13,12)
MONSTERLIST[13].MONSTER("Basilisk","Dessert",52,15)

def PickingMonsters(count):
    monsterChoosen = []
    monnList = RatingPicking()
    while count > 0:
        print("hello")
        count -= CHALLANGETOEXPDIC.get(monnList[random.randint()].chalangeRating)


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

    diffDic = {"easy" :25,"medium":50,"hard":75,"deadly":100 }
    playerDic = { 1:1, 2:1.2,3:1.3,4:1.35,5:1.35,6:1.40,7:1.45,8:1.55 }
    LevelDic = { 1: math.log(20,10),2:math.log(19,10) ,3:math.log(18,10) ,4:math.log(17,10) ,5:math.log(16,10) ,6:math.log(15,10) ,7:math.log(14,10) ,8:math.log(13,10) ,9:math.log(12,10) ,10:math.log(11,10) ,11:math.log(10,10) ,12:math.log(9,10) ,13:math.log(8,10) ,14:math.log(7,10) ,15:math.log(6,10) ,16:math.log(5,10) ,
                17:math.log(4,10) ,18:math.log(3,10) ,19:math.log(2,10) ,20:math.log(1,10) }

    userInput = input("what Difficulty do you want, Easy, Medium, Hard, or Deadly\n")
    userInput2 = input("how many players.\n")
    userInput3 = input("what average level of the player.\n")
    monList=[]

    challageCounter = 0

    for x in range(int(userInput3)):
        challageCounter = diffDic.get(userInput)*LevelDic.get(int(userInput3))

    print(challageCounter*diffDic.get(userInput))

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