# 3.- Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “abc123..” se indica “Has entrado al sistema”, 
# si no es así se da un error de usuario y/o contraseña no válidos.

import hashlib
import getpass
import subprocess

usuario = 'pepe'
password = 'abc123..' 
passCifrado = hashlib.sha512(password.encode()).hexdigest() 

# print (passCifrado)

print ("Inicio de sesión de usuario")
subprocess.call ('clear', shell=True)
u= input ("Usuario: ")
p= hashlib.sha512(getpass.getpass("Password: ").encode()).hexdigest()

# print (f"Usuario : {u} password: {p}")

if (u== usuario) and (p==passCifrado):
    print ('Has entrado al sistema')
else: 
    print ('Error de usuario y/o contraseña no válidos') 