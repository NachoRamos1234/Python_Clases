
pw = str("Hola")
while True:
    usuario = str(input("Por favor ingrese una contraseña: "))
    if (usuario != pw):
        usuario = str(input("Por favor ingrese una contraseña: "))
    elif (usuario == pw):
        print("La contraseña es correcta")
        break
