def registro(base):
  while True:
    usuario = input("Indique usuario para registrar: ")
    password = input("Indique contraseña para registrar: ")

    if usuario not in base:
      base[usuario] = password
      print(f"Registro exitoso! Usuario: {usuario}, Contraseña: {password}")
      break
    else:
      print(f"El usuario {usuario} ya existe, intente con otro nombre de usuario")
      
      
BD = {}

registro(BD)

def leer_base(base):
  print("Debajo se detalla el listado de usuarios y sus contraseñas")
  for usuario, password in base.items():
    print(f"Usuario: {usuario}, Contraseña: {password}")

leer_base(BD)

def inicio_sesion(base):
  while True:
    user = input("Ingrese usuario para iniciar sesion: ")
    passw = input("Ingrese contraseña para iniciar sesion: ")

    if user in base and passw == base[user]:
      print("Ingreso exitoso")
      break
    elif user in base and passw != base[user]:
      print("Contraseña incorrecta, intente de nuevo")
    else:
      print("Usuario no reconocido, intente de nuevo")

inicio_sesion(BD)

ruta = '/Users/paulaminassian/Library/CloudStorage/OneDrive-Personal/ENTREGA2'

def guardar(base):
  with open(ruta + "/usuarios.txt", "w") as archivo_usuarios:
    for usuario, password in base.items():
      archivo_usuarios.write(f"Usuario: {usuario}, contraseña {password} \n")
    print("Guardado de usuario en backup existoso!")

guardar(BD)