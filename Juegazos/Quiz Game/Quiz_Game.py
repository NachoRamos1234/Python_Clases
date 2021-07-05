puntaje=0
intentos=0
quiz={
    "Como se llama el pibe mas capo del mundo?: ":"Nacho",
    "Cuanto es 2+2: ":"4",
    "Quien es la mas puta de todas las putas: ":"Ella",
    "Quien es el mas pija de toda la utn: ":"Naso",
    "En un 1v1 de fort, quien gana, chocha o rasta: ":"Chocha"
}
for pregunta,respuesta in quiz.items():
    res = str(input(pregunta))
    res = res.title()
    if(res!=respuesta):
        while True:
            intentos+=1
            res = str(input(pregunta))
            res=res.title()
            if (res == respuesta):
                print(f"Correcto")
                intentos = 0
                puntaje += 1
                break
            elif (intentos == 2):
                print(f"Perdiste tus chances capo, pasa a la siguiente")
                intentos=0
                break
    elif (res == respuesta):
        print(f"Correcto")
        intentos = 0
        puntaje += 1
print(f"Tu score final es: {puntaje}")
print(f"Gracias por jugar putita sumisa")
print(f"Deseas ver la sorpresa?:")
print(f"a = si")
print(f"b = no")
lol=str(input(f"Que decidis capo?: "))
if (lol=="a"):
    while True:
        print(f"pete")
else:
    while True:
        print(f"Sos un cagon")
