#Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre “tabla-n.txt”
# la tabla de multiplicar de ese número, donde “n” es el número introducido.

n = int(input("Ingrese un numero entre 1 y 10: "))
while n > 10 or n < 1:
    n = int(input("Ingrese un numero entre 1 y 10: "))

def funcion (n):
    arch = open("tabla-n.txt", "w")
    for x in range(0,11):
        resultado = (x*n)
        arch.write(str(resultado)+"\n")
    arch.close()
funcion(n)
