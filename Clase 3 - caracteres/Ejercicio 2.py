# Pedirle al usuario que ingrese su nombre y apellido en diferentes variables, y nosotros tenemos que devolverle un
# mensaje como el siguiente “Bienvenido al sistema, Schettino Matias”. Tener en cuenta los espacios al momento de
# devolver el mensaje.

nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))

print("Bienvenido al sistema " + nombre + " " + apellido)