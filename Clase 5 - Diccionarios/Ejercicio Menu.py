print ("Bienvenido al programa")
print ("1. Agregar datos")
print ("2. Buscar datos")
print ("3. Borrar datos")
print ("4. Listar datos")
print ("0. Salir")

#ABML (español) o REST (ingles)

agenda = {}
while True:
    opcion = int(input("Ingrese una opcion"))
    if (opcion == 1):
        nombre = str(input("Ingrese un nombre"))
        nombre = nombre.title()
        if (nombre in agenda.keys()):
            print ("El numero de telefono de", nombre,"es",agenda[nombre])
        else: 
            telefono = int(input("Ingrese un numero de telefono"))
            agenda[nombre] = telefono
    elif (opcion == 2):
        contador = 0
        busqueda = str(input("Ingrese su busqueda"))
        busqueda = busqueda.lower()
        for clave, valor in agenda.items():
            clave2 = clave.lower()
            if (clave2.startswith(busqueda) or (clave2.find(busqueda)>=0)):
                print (clave,":",valor)
                contador += 1
        if (contador == 0):
            print ("No se encontro ningun dato")
    elif (opcion == 3):
        nombre = str(input("Ingrese un nombre"))
        nombre = nombre.title()
        if (nombre in agenda.keys()):
            del(agenda[nombre])
            print ("El usuario",nombre,"se ha eliminado correctamente")
        else:
            print ("No se encontro el usuario")
    elif (opcion == 4):
        for clave, valor in agenda.items():
            print (clave,":",valor)
    elif (opcion == 0):
        break
