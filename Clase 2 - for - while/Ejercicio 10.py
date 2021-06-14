
desaprobados =0
aprobados = 0
for x in range (0,10):
    nota = float(input("Por favor ingrese la nota: "))
    if (nota <= 6):
        desaprobados += 1
    elif (nota >=7):
        aprobados += 1
print("Alumnos desaprobados: ", desaprobados)
print("Alumnos aprobados: ", aprobados)