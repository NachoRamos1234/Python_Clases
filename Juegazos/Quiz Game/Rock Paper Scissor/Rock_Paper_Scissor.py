import random

print(f"Bienvenido a piedra, papel o tijera")
print(f"A: Player vs AI")
print(f"B: Player 1 vs Player 2")
op=str(input("Eleccion: "))
op=op.title()

if (op=="A"):
    print(f"\nPiedra\nPapel\nTijera\n")
    user=str(input("Ingrese su eleccion: "))
    user=user.title()
    elec=""
    pc=random.randint(1,3)
    if (pc==1):
        elec="Piedra"
    elif (pc==2):
        elec = "Papel"
    elif (pc==3):
        elec = "Tijera"
    while True:
        if(user==elec):
            print(f"La PC eligio {elec}, Empataron!")
            break
        elif(user=="Piedra" and elec=="Tijera"):
            print(f"La PC eligio {elec}, Ganaste!")
            break
        elif(user=="Papel" and elec=="Piedra"):
            print(f"La PC eligio {elec}, Ganaste!")
            break
        elif(user=="Tijera" and elec=="Papel"):
            print(f"La PC eligio {elec}, Ganaste!")
            break
        elif(user=="Piedra" and elec=="Papel"):
            print(f"La PC eligio {elec}, Perdiste!")
            break
        elif(user=="Papel" and elec=="Tijera"):
            print(f"La PC eligio {elec}, Perdiste!")
            break
        elif(user=="Tijera" and elec=="Piedra"):
            print(f"La PC eligio {elec}, Perdiste!")
            break
        elif(user!="Tijera" and user!="Papel" and user!="Piedra"):
            print(f"No ingreso una opcion valida")
            break
elif (op=="B"):
    while True:
        print(f"\nPiedra\nPapel\nTijera\n")
        ply1=str(input("Ingrese su eleccion: "))
        ply1=ply1.title()
        if (ply1 != "Tijera" and ply1 != "Papel" and ply1 != "Piedra"):
            print(f"No ingreso una opcion valida")
            break
        ply2 = str(input("Ingrese su eleccion: "))
        ply2=ply2.title()
        if (ply2 != "Tijera" and ply2 != "Papel" and ply2 != "Piedra"):
            print(f"No ingreso una opcion valida")
            break

        elif (ply1 == ply2):
            print(f"Empataron!, ambos eligieron {ply1}")
            break
        elif (ply1 == "Piedra" and ply2 == "Tijera"):
            print(f"Gano Player 1, eligio {ply1}")
            break
        elif (ply1 == "Papel" and ply2 == "Piedra"):
            print(f"Gano Player 1, eligio {ply1}")
            break
        elif (ply1 == "Tijera" and ply2 == "Papel"):
            print(f"Gano Player 1, eligio {ply1}")
            break
        elif (ply1 == "Piedra" and ply2 == "Papel"):
            print(f"Gano Player 2, eligio {ply2}")
            break
        elif (ply1 == "Papel" and ply2 == "Tijera"):
            print(f"Gano Player 2, eligio {ply2}")
            break
        elif (ply1 == "Tijera" and ply2 == "Piedra"):
            print(f"Gano Player 2, eligio {ply2}")
            break

elif(op!="A" and op!="B"):
    print(f"No ingreso una opcion valida")

k=input("Apreta Enter para salir")
