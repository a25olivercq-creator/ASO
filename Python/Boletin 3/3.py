# 3.- Crear un JSON con la información de los usuarios que tienen 
# UID >= 1000 <= 60000 y UID == 0 … 
# La clave será la cuenta y los valores un diccionario con los datos : uid, grupoPrincipal, gruposSecundarios, pathHome, tamHome, shell, password (True o False).

# ”clara”:{“uid”:1001, “grupoPrincipal”:”asir”,
#  “gruposSecundarios”:[“cdrom”,”floppy”,”audio”,”dip”,”video”], 
# “pathHome”:”/home/clara”, “tamHome”:”8M”, “shell”:”/bin/bash”, 
# “password”:False},

# “otroUsuario”: {}, ...}

# 1. - Abrir el archivo /etc/passwd ... convertirlo en una lista

from subprocess import run

#Variable que vamos a llenar con los datos de los usuarios
jsonDatosUsuarios = {}
dInfoUsuario={}

dPasswd = {}

with open ('/etc/shadow') as fr:
    lShadow = fr.readlines()

for l1 in lShadow:
    ll0 = l1.strip().split(':')
    dPasswd.setdefault(ll0[0],len(ll0[1]) > 5)

with open('/etc/passwd') as fr:
    lPasswd = fr.readlines()

for l in lPasswd:
    ll = l.strip().split(':')
    # print(conta)
    uid = int(ll[2])
    if (uid >= 1000 and uid <= 60000) or (uid == 0):
        # print(ll)
        conta = ll[0]
        pathome = ll[5]
        shell = ll[6] 
        print(f"El usuario {conta} tiene uid {uid} su home es {pathome} y su shell es {shell}")

        #Vamos a descubrir el grupo principal y los secundarios de los usuarios.
        ##groups conta ------ grupoPrincipal:String ------ gruposSecundarios:lista

        comando2 = run(f'groups {conta}', 
                    shell=True,
                    capture_output=True,
                    text=True,
                    encoding="utf-8").stdout.split()

        # print (comando2)

        grupoPrincipal=comando2[2]
        print(f'El gupo principal es {grupoPrincipal}')

        gruposSecundarios = comando2[3:]
        print(f'Los grupos secundarios son {', '.join(gruposSecundarios)}')
        

        ## Vamos a descubrir el tamaño del home de cada usuario
        ## sudo du -sh [pathhome]

        comando3 = run(f'sudo du -sh {pathome}', 
                    shell=True,
                    capture_output=True,
                    text=True,
                    encoding="utf-8").stdout.strip().split('\t')


        print(comando3)
        tamaño = comando3[0]
        ruta = comando3[1]
        print (f'Su ruta {ruta} tiene un tamaño de {tamaño}')
        print('-'*100)

        # Ejemplo jsonDatosUsuarios = {
        # ”jefe”:{“uid”:1000, “grupoPrincipal”:”sudo”,
        #  “gruposSecundarios”:[“cdrom”,”floppy”,”audio”,”dip”,”video”], 
        # “pathHome”:”/home/jefe”, “tamHome”:”16M”, “shell”:”/bin/bash”, 
        # “password”:True},

        #Completamos el json datosusuarios
        
        dInfoUsuario.setdefault("uid",uid)
        dInfoUsuario.setdefault("grupoPrincipal",grupoPrincipal)
        dInfoUsuario.setdefault("gruposSecundarios",gruposSecundarios)
        dInfoUsuario.setdefault("pathHome",pathome)
        dInfoUsuario.setdefault("tamHome",tamaño)
        dInfoUsuario.setdefault("password",dPasswd[conta])
        #Añadimos el usuario al json
        jsonDatosUsuarios.setdefault(conta, dInfoUsuario)

    else:
        pass

#Comprobamos como quedo el json con todos los datos

print(jsonDatosUsuarios)

print("Dame un nombre de usuario y te devuelvo sus datos: ")
u = input("Nombre de Usuario: ")
if u in jsonDatosUsuarios:
    print(jsonDatosUsuarios[u])
    # print(f'El usuario {u} tiene en su home {jsonDatosUsuarios[u]["tamHome"]}')


