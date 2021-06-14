sueldo = float(input("Ingrese su sueldo: "))
edad = float(input("Ingrese su edad: "))

if((sueldo > 25000.0) and (edad >= 20)):
    print("Debe pagar impuestos")
elif(edad > 30):
    print("Debe pagar impuestos")
else:
    print("No debe pagar impuestos")