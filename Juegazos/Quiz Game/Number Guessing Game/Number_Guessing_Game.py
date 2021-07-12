import random
import math

print(f"Bienvenido al juego de la Chocha!")
print(f"Vas a tener que elegir dos numeros los cuales van a ser tu rango de busqueda.")
print(f"El programa seleccionara un numero al azar dentro de ese rango y vos vas a tener que descrubrir que numero es.")
print(f"Cuantas menos suposiciones uses mejor va a ser capo, no seas govir")
print(f"Si llegas al limite de suposiciones... PERDES")
print(f"Buena suerte!")

low=int(input("Por favor ingrese su limite inferior: "))
upp=int(input("Por favor ingrese su limite superior: "))

num=random.randint(low,upp)
min=math.log(upp - low + 1, 2)
min=math.ceil(min)

print(f"Solo tenes {min} suposiciones para adivinar!")
guess = 0
while True:
    answ=int(input("Suposicion: "))
    if (answ == num):
        print(f"Ganaste... No fue tan dificil viste capo?")
        print(f"Suposiciones: {guess}")
        break
    elif (guess == (min-1)):
        print(f"Perdiste pa, el numero era: {num}")
        print(f"Mejor suerte la proxima")
        break
    elif(answ>num):
        guess+=1
        print(f"Volve a intentar! Tiraste muy alto malo")
    elif(answ<num):
        guess+=1
        print(f"Volve a intentar! Tiraste muy bajo malo")
k=input("Apreta Enter para salir")