"""
INTERPRETERANDE SPRÅK = ingen kompilering i förtid
"script"
# """

# Loopar
#        - "FOR EACH" for x in range()
years = range(1972,2023)
for i in years:
    print(i)

for i in range(1972,2023):
    print(i)     

for i in range(2023,1972,-4):
    print(i)     


killarna = ["Stefan", "Oliver", "Stellan", "Musse"]
x = 0
for namn in killarna:
    x = x + 1
    print(f"Skriver namn {x}")
    print(namn)
    print("Hej")


# while True:
#     x = int(input("Ange ett tal"))
#     if x == 0:
#         break


# Listor
#       - []   växer/krymper oändligt
#       objektorienterad syntax - listan.append(...)
#       vad som helst i den
killarna = []
killarna.append("Stefan")
killarna.append("Kalle")
killarna.append("Nisse")
antal = len(killarna)

# MAP   Algoritmer + datastrukturer
#      dictionary {} =    
#killarna[""]

# spelarna = {} # mappning mellan en sak och en annan
# spelarna[13] = "Mats Sundin"
# spelarna[21] = "Peter Forsberg"

banken = {}
banken["123-1212 123"] = 500
banken["123-1212 999"] = 400

def menu():
    print("1. Ange namn")
    print("2. Exit")

menu()

def calculateSalary(namn:str, hourlySalary:float, hoursWorked:int) -> float :
    salary = hourlySalary * hoursWorked
    if namn == "Stefan":
        salary += 1000
    return salary

res = calculateSalary("Stefan",127.5,1)

res = calculateSalary("Kalle", 100, 10)    
res = calculateSalary("Stefan", 100, 10)    
res = calculateSalary(12, "Kaller", 5)

# Functions + type hinting (  https://docs.python.org/3/library/typing.html )
#           def ... parametrar + return
# # Klasser  "STRUCTS"
#  Klass = OOP -> klass kan innehålla funktioner och fält
#               struct = bara fält
#          https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass   

@dataclass
class Employee:
    Namn:str
    Age:int
    HourlySalary:int

listOfEmployees = []
stefan = Employee("Stefan", 50, 100)
stefan.Age = stefan.Age + 1
if stefan.Namn == "Kalle":
    print("Hej")
listOfEmployees.append(stefan)    
listOfEmployees.append(Employee("Oliver", 14, 20))









# skapa en THUMBNAIL av en stor bild?         
# ladda ner en stor/fin bild ex https://pixabay.com/photos/hockey-sport-athlete-player-puck-2180834/
# lägg den i denna folder
# PIP install 
# https://pypi.org/project/Pillow/
size = (200,150)
from PIL import Image
image = Image.open("hockey-2180834_1920.jpg")
image.thumbnail(size)
image.save("lillabilden.jpg")

while True:
    namn = input("Vad heter du?")
    # strlen
    l = len(namn)
    if l >- 1:
        break
    print("Skriv in lite längre tack")

i = i  + 1 

namn = namn.upper()
namn = namn.replace("läxa", "****")
namn = namn.replace("grönsaker", "****")

# if namn.find("läxa") != -1:
#     print("Fult ord")

print(f"Ditt namn börjar på {namn[0]}")

print("ccc")    



n = "S"
n += "tefan"

n = n * 10
print(n)

y = 0.1   #0.0999999998
y = 12.12343
y = y + 12




if y + y + y == 0.3:
    print("Hej")

#pr
# 
# x =int("Vad heter du?")
# 'citat "r3wr4"  dwsad'
namn = input('Vad heter du')
age = input("Hur gammal är du?")
age = int(age)
age = age + 1
namn = 1234
print(f"Hej {namn} kul att du är {age} år")





namn = "Stefan"
namn = namn + " Holmberg"
age = 12
age = age + 1

# Hej Stefan Holmberg kul att du är 13 år

print("Hej " + namn + " kul att du är " + str(age) + " år")
print(f"Hej {namn} kul att du är {age} år")






