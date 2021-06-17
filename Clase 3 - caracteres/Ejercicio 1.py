
#Pedirle al usuario que ingrese una cadena, debemos preguntarnos si la cadena ingresada
#tiene 10 o mas caracteres, si es asi devolver un mensaje que diga “Su cadena tiene 10 o
# mas caracteres”, sino, “Su cadena es muy corta”

cadena = str(input("Ingrese una cadena: "))
longitud = len(cadena)
if (longitud >= 10):
    print("Su cadena tiene 10 o mas caracteres")
else:
    print("Su cadena es muy corta")
    