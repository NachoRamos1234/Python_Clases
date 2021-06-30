#Crear un programa que permita ingresarle 2 números al usuario. Estos dos numeros se
#deben sumar, restar, multiplicar y dividir.
#Para esto se deben crear 4 funciones:
#-suma
#-resta
#-multiplicacion
#-divison
#Cada función debe tener 2 parámetros y devolver un resultado para luego imprimirlo
#en pantalla.

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un numero: "))

def suma(numero1, numero2):
    resultado = numero1+numero2
    return resultado
def resta(numero1, numero2):
    resultado = numero1-numero2
    return resultado
def multiplicacion(numero1, numero2):
    resultado = numero1*numero2
    return resultado
def division(numero1, numero2):
    resultado = numero1/numero2
    return resultado

a=suma(numero1,numero2)
print(a)
b=resta(numero1,numero2)
print(b)
c=multiplicacion(numero1,numero2)
print(c)
d=division(numero1,numero2)
print(d)