
frutas = {"banana": 135, "manzana":80, "pera":85, "naranja":70}
while True:
    fruta=str(input("Ingrese una fruta: "))
    if fruta in frutas.keys():
        print("El valor es:", frutas[fruta])
    else:
        print("Lo siento la fruta",fruta,"no esta disponible")