
print("Bienvenido al programa: ")
print("1. Agregar comidas al menu")
print("2. Comprar")
print("3. Ver menu")
print("0. Exit")
menu={}
acumulador = int(0)
while True:
    opcion = int(input("Ingrese una opcion: "))
    if (opcion == 1):
        comida = str(input("Ingrese una comida: "))
        comida = comida.title()
        precio = str(input("Ingrese un precio: "))
        if comida in menu.keys():
            print("La comida ya se encuentra en el menu")
        else:
            menu[comida] = precio
    elif (opcion == 2):
        while True:
            print("0. Exit")
            print("1. Comprar")
            opcion2 = int(input("Ingrese una opcion: "))
            if (opcion2 == 1):
                compra = str(input("Que comida desea comprar? "))
                compra=compra.title()
                cantidad = int(input("Cuantas unidades va a llevar? "))
                if compra in menu.keys():
                    compra2 = int(menu[compra])
                    total = (compra2 * cantidad)
                    acumulador = acumulador + total
                else:
                    print("Error, la comida no se encuentra en el menu")
            elif (opcion2 ==0):
                break
        print("Su total es:",acumulador)
    elif (opcion ==3):
        for clave, valor in menu.items():
            print (clave,":",valor)
    elif (opcion == 0):
        break
