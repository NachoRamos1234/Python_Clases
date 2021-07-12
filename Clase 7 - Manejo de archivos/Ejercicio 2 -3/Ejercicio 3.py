#Una vez que “números.txt” este cargado por el ejercicio dos, hacer un programa nuevo que lea todo ese archivo y
#devuelva el valor total de los números ingresados y el promedio de todos estos.

arch = open("numeros.txt","r")
total = 0
contador = 0
promedio = 0
next(arch)
for linea in arch:
    linea = int(linea)
    total = total + linea
    contador += 1
    promedio = total/contador

arch.close()
print(f"El total es: {total}")
print(f"El promedio es: {promedio}")
