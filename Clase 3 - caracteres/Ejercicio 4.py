#Ingresar una cadena y verificar si esta se encuentra escrita toda en minúscula, si es así devolver “Su cadena esta
# bien escrita”, sino, un mensaje que diga “Por favor ingrese toda la cadena en minúscula”

cad = str(input("Ingresar una cadena: "))

if (cad == cad.lower()):
    print("Su cadena esta bien escrita")
else:
    print("Por favor ingrese toda la cadena en minuscula")
    