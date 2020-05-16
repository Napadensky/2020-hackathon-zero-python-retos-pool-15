from random import randint

options = ["piedra", "papel", "tijeras"]
print('------------------START---------------')
# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    resultado = "---"
    if player == ai:
        print("\nEmpate")
        resultado = "Empate"

    if player == "tijeras":
        if ai == "papel":
            print('\n'+'>> GANASTE <<')
            resultado = "Player"
        if ai == 'piedra':
            print('\n'+'>> PERDISTE <<')
            resultado = "A.I."

    if player == "piedra":
        if ai == "papel":
            print('\n'+' >> PERDISTE <<')
            resultado = "A.I."
        if ai == "tijera":
            print('\n'+'>> GANASTE <<')
            resultado ="Player"

    if player == "papel":
        if ai == "tijera":
            print('\n'+'>> PERDISTE <<')
            resultado = "A.I."
        if ai == "piedra":
            print('\n'+'>> GANASTE <<')
            resultado ="Player"

    print("Eleccion de la PC: --",ai," --")

    return resultado

# Entry Point
def Game():
    #
    #
    player = input("Elige > Piedra - Papel - Tijeras < : ").lower()
    while player != "piedra" and player != "papel" and player != "tijeras":
        print("\n-NO ELEGISTE UNA DE LAS OPCIONES-. ELIGE ENTRE PIEDRA, PAPEL O TIJERA")
        player = input("Elige Piedra - Papel - Tijera: ").lower()
        
    print("\nPlayer eligio fue: -- ", player," --")
    rm = randint(0, 2)
    ai = options[rm]
    # quienGana(player,ai)
    #
    #
    
    winner = quienGana(player, ai)

    print("El ganador es: ",winner)

Game()