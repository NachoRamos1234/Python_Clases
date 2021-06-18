#Ingresar una cadena, si esta tiene mas de 7 caracteres imprimir un mensaje diciendo “Su cadena es muy larga, su nueva
# cadena será X”, donde X es igual a las primeras 3 letras de esa cadena.

cad = str(input("Ingrese una cadena: "))

if (len(cad) > 7):
    x = cad[0:3]
    print("Su cadena es muy larga, su nueva cadena sera " + x)
else:
    print("Su cadena es correcta")