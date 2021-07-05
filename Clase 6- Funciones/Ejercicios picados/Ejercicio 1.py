#Se debe crear una funcion llamada validar que devuelva 1 o 0 dependiendo de si el registro es exitoso
#Para que el registro sea verdadero se tiene que cumplir:
#El numero de telefono debe tener si o si 10 caracteres, y solo pueden ser numeros
#El mail debe ser un mail valido, osea tener @
#El DNI debe tener 7 u 8 caracteres
#La contraseña debe tener al menos 1 mayuscula, 1 minuscula y 6 caracteres
#Ambas contraseñas deben coincidir

def validar(diccionario):
    error = 0
    mensaje = ""
    
    nombre = diccionario['nombre']
    apellido = diccionario['apellido']
    telefono = diccionario['telefono']
    correo = diccionario['correo']
    dni = diccionario['dni']
    pw = diccionario['pw']
    pw2 = diccionario['pw2']

    telefono = str(telefono)
    dni = str(dni)

    if (len(telefono) != 10):
        error = 1
        mensaje += "Su telefono es invalido."+"\n"

    if not('@' in correo):
        error = 1
        mensaje += "Su email es invalido."+"\n"

    if (len(dni)!=7 and len(dni)!=8):
        error = 1
        mensaje += "Su DNI es invalido."+"\n"

    if (pw.upper() == pw):
        error = 1
        mensaje += "Su contraseña no tiene minuscula."+"\n"

    if (pw.lower() == pw):
        error = 1
        mensaje += "Su contraseña no tiene mayusculas."+"\n"

    if (len(pw)<6):
        error = 1
        mensaje += "Su contraseña debe tener al menos 6 caracteres."+"\n"

    if (pw != pw2):
        error = 1
        mensaje += "Sus contraseñas no coinciden."+"\n"        

    return error, mensaje

d = {}

nombre = input("Ingrese su nombre")
apellido = input("Ingrese su apellido")
telefono = int(input("Ingrese su telefono"))
correo = input("Ingrese su email")
dni = int(input("Ingrese su DNI"))
pw = input("Ingrese su contraseña")
pw2 = input("Valide su contraseña")

d['nombre'] = nombre.strip()
d['apellido'] = apellido.strip()
d['telefono'] = telefono.strip()
d['correo'] = correo.replace(" ", "")
d['dni'] = dni.strip()
d['pw'] = pw.strip()
d['pw2'] = pw2.strip()

error, mensaje = validar(d)
if (error == 1):
    #redigis a otra pagina
if (error == 0):
    #no haces nada

