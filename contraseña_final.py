
user = "peter"
password = "12345"

usuario = input('ingrese usuario:  ' )

if user == usuario:
    contraseña = input('ingrese contraseña: ')
    
    if contraseña == password and usuario == user:
      print("acceso permitido")
    else:
     print("acceso denegado")

else:
    print("datos invalidos")
    


