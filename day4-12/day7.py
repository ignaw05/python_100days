#hangman
import random
vidas = 6
palabras = ["ventana", "camino", "estrella", "jardín", "cancion", "arbol", "viento", "tierra", "amistad", "puente"]
aciertos = []
palabra = ''

palabra_adiv = random.choice(palabras)

def inicializar():
    for i in range(0,len(palabra_adiv)):
        aciertos.append('_')
    act_str(palabra)

def act_str(palabra):
    for i in aciertos:
        palabra += i
    print(f"La palabra es: {palabra}")
    

def pedir(vidas):
    while(vidas > 0):
        guess = str(input("Ingrese una letra: "))
        if guess in palabra_adiv:
            cont = 0
            for i in palabra_adiv:
                if guess == i:
                    aciertos[cont] = guess
                cont += 1
            print(f"\nLa letra {guess.capitalize()} esta en la palabra")
            act_str(palabra)
            print(f"Quedan {vidas} vidas\n")

            if '_' not in aciertos:
                print("\nGanaste el juego")
                break
            
        else: 
            print(f"La letra {guess.capitalize()} NO esta en la palabra")
            act_str(palabra)
            vidas = vidas - 1
            print(f"Quedan {vidas} vidas\n")
            if vidas == 0:
                print("\nGAME OVER HDP")

inicializar()
pedir(vidas)






