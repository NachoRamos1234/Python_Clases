# Crear un programa que le permita al usuario ingresar un numero y que le devuelva
# la tabla del 10 de ese numero. Para esto se debe usar la función –tabla

numero=int(input("Ingrese un numero: "))
def tabla(numero):
    for x in range(1,11):
        resultado = (numero*x)
        print(resultado)
a=tabla(numero)
print(a)

def tabla(numero):
    lista=[]
    for x in range(1,11):
        resultado = (numero*x)
        lista.append(resultado)
    return lista
