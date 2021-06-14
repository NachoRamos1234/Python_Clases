
contador = 0
while True:
    num = int(input("Ingrese un numero valido: "))
    if num > 0:
        print("El numero", num, "es valido")
        contador += 1
    elif num <= 0:
        print("El numero", num, "no es valido")
    if (contador == 9):
        break
