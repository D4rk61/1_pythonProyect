# !/usr/bin/python
# Programa para el juego de piedra, papel o tijera
# Con condicionales

# Paso 1. Agregar las condicionales y los if anidados

import random


options = ("piedra", "papel", "tiejra")
computer_wins = 0
user_wins = 0 

rounds = 1 

while True:

    print(f"""
        
        Juego Piedra, Papel o Tijera
        
        ----------------------------
          Numero de ronda {rounds}
        ----------------------------

        """)

    print(f"victorias del computador > {computer_wins}")
    print(f"victorias del usuario > {user_wins}")
    user_opt = str(input("""
        Ecoge:
    
            1-) piedra 
            2-) papel
            3-) tijera
    
    >> """))
    user_opt = user_opt.lower()
    print()
    if not user_opt in options:
        print("Opcion Incorrecta :(")
    
    pc_opt = random.choice(options)

    print("Opcion del usuario >> ", user_opt)
    print("Opcion del pc >> ", pc_opt)
    
    print()
    if user_opt == pc_opt:
        print("Empate!")
    elif user_opt == "piedra":
        if pc_opt == "tijera":
            print("Piedra mata a tijera")
            print()
            print("Usuario Gano!")
            user_wins += 1
        else:
            print("Papel mata a piedra")
            print("Pc gana")
            computer_wins += 1
    
    elif user_opt == "papel":
        if pc_opt == "piedra":
            print("papel gana a piedra")
            print()
            print("Usuario Gano!")
            user_wins += 1
        else:
            print("tijera gana a papel")
            print()
            print("PC Gana!")
            computer_wins += 1
    
    elif user_opt == "tijera":
        if pc_opt == "papel":
            print("tijera gana a papel")
            print()
            print("Ususario Gano!")
            user_wins += 1
        else:
            print("piedra gana a tijera")
            print()
            print("PC Gano!")
            computer_wins += 1

    if computer_wins == 3:
        print("""

            El ganados es la computadora, Bien Jugado!

            """)
        break

    if user_wins == 3:
        print("""
            
            Eres el Ganador!   ¡Felicidades!

            """)
        break
    rounds += 1
