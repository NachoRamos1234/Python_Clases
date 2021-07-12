import random
import click

def validate(self, ctx, input):
    input = input.title()
    if input == "Piedra":
        return input
    elif input == "Papel":
        return input
    elif input == "Tijera":
        return input
    else:
        raise click.BadParameter("Not a valid input")

@click.command()
@click.option("--user", prompt="\nPiedra\nPapel\nTijera\n\nElegi wachin ", callback=validate)
def ai(user):
    pc = random.choice(["Piedra", "Papel", "Tijera"])
    resultado = quien_gano(user, pc)
    resultado_en_pantalla("A", resultado,pc)

@click.command()
@click.option("--ply1", prompt="\nPiedra\nPapel\nTijera\n\nElegi wachin jugador 1", callback=validate)
@click.option("--ply2", prompt="Elegi wachin jugador 2", callback=validate)
def pvp(ply1, ply2):
    pc = None
    resultado = quien_gano(ply1, ply2)
    resultado_en_pantalla("B", resultado,pc)

def quien_gano(ply1, ply2):
    opciones={"Piedra":0, "Papel":1, "Tijera":2}
    ply1=opciones[ply1]
    ply2 = opciones[ply2]
    if ply1 == ply2:
        return 0
    elif (ply1 - ply2) % 3 == 1:
        return 1
    else:
        return 2

def resultado_en_pantalla(op, resultado,pc):
    if op == "A":
        if resultado == 0:
            print("Empate")
        elif resultado == 1:
            print(f"Ganaste, la PC eligio {pc}")
        else:
            print(f"Gano la PC, , la PC eligio {pc}")
    else:
        if resultado == 0:
            print("Empate")
        elif resultado == 1:
            print("Gano jugador 1")
        else:
            print("Gano jugador 2")

    input("Apreta Enter para salir")

def main():
    print(f"Bienvenido a piedra, papel o tijera")
    print(f"A: Player vs AI")
    print(f"B: Player 1 vs Player 2")
    op = click.prompt("Eleccion", type=str)
    op = op.title()

    if op == "A":
        ai()
    elif op == "B":
        pvp()
    else:
        print(f"No ingreso una opcion valida")
        input("Apreta Enter para salir")

if __name__ == "__main__":
    main()