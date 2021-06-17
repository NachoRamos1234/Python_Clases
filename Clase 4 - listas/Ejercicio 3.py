# Pedirle al usuario que cargue 2 listas de 5 nombres, después preguntarte cuales son los nombres de la segunda lista
# que se encuentran en la primera, por ejemplo:
# lista_uno [“nombre1”, “nombre2”, “nombre3”, “nombre4”, “nombre5”]
# lista_dos[“nombre1, “nombre4”, “nombre7”, “nombre2”, “nombre10”]
#Despues de toda la lógica, el programa debería devolver “Los nombres que se repiten son nombre1, nombre2, nombre4


list1=[]
list2=[]
list3=[]
for x in range (0,5):
    nombre1 = str(input("Ingrese un nombre para la primer lista: "))
    list1.append(nombre1)
for x in range (0,5):
    nombre2 = str(input("Ingrese un nombre para la primer lista: "))
    list2.append(nombre2)
for elemento in list2:
    if elemento in list1:
        list3.append(elemento)
print("Los nombres repetidos son", list3)
