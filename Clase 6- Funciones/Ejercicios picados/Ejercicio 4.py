lista=[]
for x in range (0,5):
    num=int(input("Ingrese un numero: "))
    lista.append(num)
def separar (lista):
    pares=[]
    impares=[]
    for x in lista:
        if (x==0):
            print("El numero 0 no es par ni impar")
        elif ((x%2)==0):
            pares.append(x)
        elif ((x%2)!=0):
            impares.append(x)
    return pares, impares

pares,impares=separar(lista)
print("Los numeros pares son:",pares)
print("Los numeros impares son:",impares)
