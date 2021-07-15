
def obtener_lista():
    archivo = open("puntajes.txt", "r")
    alumnos = []
    for linea in archivo:
        linea = int(linea.strip())
        alumnos.append(linea)
    archivo.close()
    return alumnos

def clasificar_listas(alumnos):
    aceptados = []
    rechazados = []
    alumnos.sort(reverse=True)
    for nota in range(0, 849):
        aceptados.append(alumnos[nota])
    for nota in range(850, len(alumnos)):
        rechazados.append(alumnos[nota])
    return aceptados, rechazados

def calcular_becas(aceptados):
    contador = 0
    for nota in aceptados:
        if int(nota) >= 764:
            contador += 1
    coste = contador * 10000
    return coste

def puntaje_promedio(aceptados):
    acumulador = 0
    for nota in aceptados:
        acumulador += nota
    promedio = acumulador/len(aceptados)
    return promedio

print("Bienvenido al menu")
print("1. Listar alumnos")
print("2. Notas de aceptados y rechazados")
print("3. Coste de beca")
print("4. Nota promedio de alumnos aceptados")
print("0. Exit")

opcion = int(input("Ingrese su opcion: "))
while opcion != 0:
    if opcion == 1:
        print("Las notas son: ")
        alumnos = obtener_lista()
        for linea in alumnos:
            print(linea)
    elif opcion == 2:
        alumnos = obtener_lista()
        aceptados, rechazados = clasificar_listas(alumnos)
        print("La nota de los alumnos aceptados son: ")
        for linea in aceptados:
            print(linea)
        print("La nota de los alumnos rechazados son: ")
        for linea in rechazados:
            print(linea)
    elif opcion == 3:
        alumnos = obtener_lista()
        aceptados, rechazados = clasificar_listas(alumnos)
        coste = calcular_becas(aceptados)
        print(f"La cantidad mensual que la escuela debera pagar es de ${coste}")
    elif opcion == 4:
        alumnos = obtener_lista()
        aceptados, rechazados = clasificar_listas(alumnos)
        promedio = puntaje_promedio(aceptados)
        print(f"La nota promedio de los alumnos que ingresaron es {promedio}")
    opcion = int(input("Ingrese su opcion: "))
