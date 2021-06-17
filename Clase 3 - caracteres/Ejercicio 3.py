#El usuario debe ingresar 2 cadenas y debemos preguntarnos si la segunda cadena esta dentro de la primera, si es asi
# debemos devolver un mensaje “Su segunda cadena se encuentra en la primera”

cad1 = str(input("Ingrese una cadena: "))
cad2 = str(input("Ingrese otra cadena: "))

if cad2 in cad1:
    print("Su segunda cadena se encuentra en la primera")
else:
    print("Su segunda cadena no se encuentra en la primera")