import random
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def sumar(mazo):
    total = 0
    for i in mazo:
        total += i
    return total
            
def verificar(miTotal):
        if miTotal > 21:
            if 11 in miMano:
                miMano[miMano.index(11)] = 1
                miTotal = sumar(miMano)
                verificar(miTotal)
            else:
                print(f"Mis cartas: {miMano}, total actual: {miTotal}\n")
        return miTotal

def verif_c(suTotal,manoCrup):
        while suTotal < 17 :
            manoCrup.append(random.choice(cards))
            suTotal = sumar(manoCrup)
        print(f"Cartas croupier: {manoCrup}, total actual: {suTotal}")
        if suTotal > 21:
            if 11 in manoCrup:
                    manoCrup[manoCrup.index(11)] = 1
                    suTotal = sumar(manoCrup)
                    verif_c(suTotal,manoCrup)
            else: print("El Croupier se pasa, ganaste!\n")
        return suTotal

while True:
    miMano = random.choices(cards,k=2)
    manoCrup = [random.choice(cards)]

    miTotal = sumar(miMano)
    suTotal = sumar(manoCrup)
    print(f"Mis cartas: {miMano}, total actual: {miTotal}")
    print(f"Cartas croupier: {manoCrup}, total actual: {suTotal}")
    ask1 = input("\nEscribe 'y' para pedir una mas, 'n' para pasar: ")
    while ask1 == 'y':
        miMano.append(random.choice(cards))
        miTotal = sumar(miMano)
        miTotal = verificar(miTotal)
        if miTotal > 21 : 
            print(f"Te pasaste! Perdiste\n")
            break
        else:
            print(f"Mis cartas: {miMano}, total actual: {miTotal}")
            print(f"Cartas croupier: {manoCrup}, total actual: {suTotal}")

            ask1 = input("Escribe 'y' para pedir una mas, 'n' para pasar: ")

    if miTotal <= 21:
        suTotal = verif_c(suTotal,manoCrup)
        if 21 >= suTotal > miTotal:
            print("\nPerdiste\n")
        elif suTotal == miTotal:
            print("\nEmpate!\n")
        else: print("\nGanaste\n")
    ask2 = input("Quieres seguir jugando? 'y' o 'n': \n")
    if ask2 == 'y':
        miMano = []
        suTotal = 0
        manoCrup = None
        miTotal = 0
        system("clear")
    else: break


