# Pedirle al usuario que agregue a una lista 5 nombres de personas, después preguntarte si el nombre “Pedro” se
# encuentra dentro de esos 5 nombres, si es así se debe mostrar un mensaje “Pedro se encuentra entre tus nombres”,
# sino, “Pedro no se encuentra entre tus nombres”

lista = []
for x in range(0,5):
    nombre = str(input("Ingrese un nombre: "))
    lista.append(nombre)
if "Pedro" in lista:
    print("Pedro se encuentra entre tus nombres")
else:
    print("Pedro no se encuentra entre tus nombres")
