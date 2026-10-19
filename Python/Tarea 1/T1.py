# Script que da de alta usuarios desde un css separado por comas

# Leemos el archivo y lo pasamos a una lista de lineas

import unicodedata
def eliminaTildes(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

from subprocess import run

# from hashlib import 

pathArchivo = './usuariosProba.csv'

with open(pathArchivo) as fr:
    lArch = fr.readlines()
# cont = 0

# print(lArch)


#### Creamos la variable grupos para los grupos secundarios de los usuarios

gsecjefe = run('groups jefe', 
               shell=True,
               capture_output=True,
               text=True,
               encoding="utf-8").stdout

# print (','.join(gsecjefe.split()[3:])) 

gsec=f'alumnos,{','.join(gsecjefe.split()[3:])}' #El join permite añadir como separedor de las secciones del split lo que pongamos antes.
print (gsec)

####

# Recorremos los usuarios que están en la lista en cada linea
for l in lArch[1:]: #Con [1:] saltamos la primera linea
    
    # print(l.strip()) #Con el strip quitamos el return
    ll = l.strip().split(';')#Convertimos la linea en una lista de campos
    # print(ll)
    # cont+=1
    conta = eliminaTildes(f'a26{ll[2]}{ll[0][0]}{ll[1][0]}{ll[7].split('/')[2]}'.replace(' ','').lower())
    #Creamos el comando para la contraseña
    passwd = run (f'openssl passwd -6 {l[6].strip}',
                shell=True,
                capture_output=True,
                text=True,
                encoding="utf-8").stdout.strip()
    #Creamos o comando que da de alta a los usuarios
    comando =f"sudo useradd -d /home/{conta} -m -g {ll[8].lower()} -G {gsec} -s /bin/bash -p '{passwd}' {conta}"
    print(150*'-')
    print(ll)
    print (conta)
    print(comando)
# print (cont)

