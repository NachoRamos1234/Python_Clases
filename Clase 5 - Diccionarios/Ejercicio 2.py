#Escribir un programa que le pregunte al usuario su nombre, su dni y su dirección.
# Almacenar esa información en un diccionario y después se debe mostrar el siguiente mensaje:
# “El usuario <nombre> de DNI <dni> vive en <dirección”

nombre = str(input("Ingrese su nombre: "))
dni = int(input("Ingrese su DNI: "))
direccion = str(input("Ingrese su direccion: "))

usuario = {}
usuario["1"]=nombre
usuario["2"]=dni
usuario["3"]=direccion

print("El usuario",usuario["1"],"de DNI",usuario["2"], "vive en", usuario["3"])





