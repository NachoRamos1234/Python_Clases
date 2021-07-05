numero=0
def factorial (numero):
    diccionario={}
    while True:
        numero = int(input("Ingrese un numero: "))
        resultado = 1
        if(numero<0):
            print("No se puede obtener el factorial de un numero negativo")
            break
        elif(numero==0):
            break
        elif (numero>0):
            for x in range(1,numero+1):
                resultado=resultado*x
                diccionario[numero]=resultado
    return diccionario
diccionario=factorial(numero)
if (len(diccionario)>0):
    for x,y in diccionario.items():
        print(x,":",y)
else:
    print("Error")
