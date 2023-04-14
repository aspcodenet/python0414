from dataclasses import dataclass
import random
from timeit import default_timer as timer
import time


# folder 


# datastrukturer och algoritmer
# linked list
# 500 000 items -> array   (om vi programmerar på PC)
# dict = map

# lista = ["Zeb", "Lisa",	"Anna",	"Martin","Tage","Stefan","Pia"]
# for outer in range(0,len(lista)):
#     for inner in range(outer+1,len(lista)):
#         if lista[outer] ... lista[inner]



@dataclass
class Player:
    Jersey = 0
    Name = ""
    Team = ""


def findPlayer(listOfPlayers, name,jersey,team):
    for p in listOfPlayers:
        if p.Jersey == jersey and p.Name == name and p.Team == team:
            return thePlayer
    return None

# ORDO har INGET med TID att göra
# O(n) 

# 1 000 000 -> 10 sekunder
# 2 000 000 -> 20 sekunder
# LINJÄR ökning av tid när antalet (  n  ) ökar

# 1 000 000 -> 5 sekunder
# 2 000 000 -> 10 sekunder
# LINJÄR ökning av tid när antalet (  n  ) ökar

allPlayers = []    
for x in range(0,1000000):
    jersey = random.randint(1, 50)
    names = "Player " + str(x)

    p = Player()
    p.Jersey = jersey
    p.Name = names
    p.Team = "Team " + str(x)
    allPlayers.append(p)

start = timer()
findPlayer(allPlayers,"Peter R", 123,"Test")
end = timer()
print(end - start) # Time in seconds, e.g. 5.38091952400282



# [13,45,23,4556,11,23,11,323]
#        23

def containDuplicates(listOfPlayers): # return true eller false
    for index1 in range(0,len(listOfPlayers)):
        p1 = listOfPlayers[index1]
        for index2 in range(index1+1,len(listOfPlayers)):        
            p2 = listOfPlayers[index2]
            if p1.Jersey ==p2.Jersey and p1.Name == p2.Name and p1.Team == p2.Team:
                return True
    return False

# a[100] = 100
# a[1] = 200

# n = ANTALET
# dict map  map -> en sak och en annan
allPlayers = []    
allPlayersDict = {}
for x in range(0,1000000):
    jersey = random.randint(1, 50)
    names = "Player " + str(x)

    p = Player()
    p.Jersey = jersey
    p.Name = names
    p.Team = "Team " + str(x)
    allPlayers.append(p)

    allPlayersDict[names] = p


# BOK  For-   0, 1,2,3,4,5  
# BOK -> Index "For"  -> 298
# Index - binary search


# accounts = {}
# accounts["123-123 344"] = 100
# accounts["123-123 123"] = 500




start = timer()
a = allPlayersDict["Player 499999"]
end = timer()
print(end - start) # Time in seconds, e.g. 5.38091952400282


start = timer()
a = allPlayers[1]
end = timer()
print(end - start) # Time in seconds, e.g. 5.38091952400282
a = allPlayers[399]



