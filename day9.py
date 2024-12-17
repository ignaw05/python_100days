from os import system
datos = {
    "Nombre" : "Ignacio Wuilloud",
    "Dni": 46398525 ,
    "Nacionalidad": "Argentina",
    "Deportes" : ["Futbol", "Windsurf", "Polo"],
    "Facultad" : {
        "Nombre" : "UTN",
        "Carrera" : "Ing en sistemas",
        "Materias" : ["Algebra", "Python"]
    }
}

#for i in datos:
#    print(f"{i} = {datos[i]}")

another = True
bidders = {}
max = 0
winner = ''

while (another):
    print("Hello, welcome to the bid")
    name = input("What is your name? ")
    bid = int(input("Bid: "))
    bidders[name] = bid
    if input("Another bid? ").lower() == "no":
        another = False
    system("clear")

for person in bidders:
    if bidders[person] > max:
        max = bidders[person]
        winner = person

print(f"The winner is {winner} with a bid of ${max}")