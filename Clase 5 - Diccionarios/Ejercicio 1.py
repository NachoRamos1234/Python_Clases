# Si tenemos el diccionario:
# metodos = {“suma”: “+”, “resta”: “-“, “multiplicacion”: “*”}
# Y la lista
# lista = [“suma”, “resta”]
# Imprimir los símbolos de las claves que estén dentro de la lista

metodos = {"suma": "+", "resta": "-", "multiplicacion": "*"}
lista = ["suma", "resta"]

for clave, valor in metodos.items():
    if clave in lista:
        print("Su valor es:", valor)
print(metodos["suma"])

