#Escribir un programa que le pida al usuario ingresar diferentes números hasta que uno de ellos sea 0. Se debe escribir
#en un archivo llamado “números.txt” todos los números pares mayores que 20.

lista=[]

arch = open("numeros.txt", "w")
arch.write("Los numeros pares mayores a 20 son: \n")

n = int(input("Ingrese un numero: "))
if n%2==0 and n>20:
    lista.append(n)
while n!=0:
    n = int(input("Ingrese un numero: "))
    if not n in lista:
        lista.append(n)
    if n%2!=0 or n<20:
        lista.remove(n)
lista.sort()
for linea in lista:
    linea=str(linea)
    arch.write(linea+"\n")
arch.close()
