#Crear la función –es_par que tenga como parámetro un numero, y dependiendo de
#este devolver 1 si es par y 0 si impar.
#Luego, fuera de la función, si esta devuelve 1 se debe mostrar un mensaje en pantalla
#“El numero ingresado es par”, sino, “El numero ingresado es impar”

numero = int(input("Ingrese un numero: "))
def es_par(numero):
    if ((numero%2)==0):
        return "1"
    else:
        return "0"
a=es_par(numero)
a=int(a)
if (a==1):
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")
