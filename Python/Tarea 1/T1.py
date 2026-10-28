# Script que da de alta usuarios desde un css separado por comas

# Leemos el archivo y lo pasamos a una lista de lineas

import unicodedata
def eliminaTildes(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

from subprocess import run, call

# from hashlib import 

pathArchivo = './usuariosProba.csv'

with open(pathArchivo) as fr:
    lArch = fr.readlines()
# cont = 0

# print(lArch)

## Pasamos los archivos de texto con los directorios a una lista para cada uno...

pathAsir = './asir.txt'

with open (pathAsir) as fr:
    lAsir = fr.readlines()


pathDaw = './daw.txt'

with open (pathDaw) as fr:
    lDaw= fr.readlines()


#### Creamos la variable grupos para los grupos secundarios de los usuarios

gsecjefe = run('groups jefe', 
               shell=True,
               capture_output=True,
               text=True,
               encoding="utf-8").stdout

# print (','.join(gsecjefe.split()[3:]))
#


gsec=f'alumnos,{','.join(gsecjefe.split()[3:])}' #El join permite añadir como separedor de las secciones del split lo que pongamos antes.
print (gsec)

####
## Ejecutando comandos

call

# Recorremos los usuarios que están en la lista en cada linea
for l in lArch[1:]: #Con [1:] saltamos la primera linea
    
    # print(l.strip()) #Con el strip quitamos el return
    ll = l.strip().split(';')#Convertimos la linea en una lista de campos
    # print(ll)
    # cont+=1
    g = ll[8].lower()
    conta = eliminaTildes(f'a26{ll[2]}{ll[0][0]}{ll[1][0]}{ll[7].split('/')[2]}'.replace(' ','').lower())
    #Creamos el comando para la contraseña
    passwd = run (f'openssl passwd -6 {ll[6].strip()}',
                shell=True,
                capture_output=True,
                text=True,
                encoding="utf-8").stdout.strip()
    #Creamos o comando que da de alta a los usuarios
    cAlta =f"sudo useradd -d /home/{conta} -m -g {g} -G {gsec} -s /bin/bash -p '{passwd}' {conta}"
    call(cAlta, shell=True)

    print(ll)
    print (conta)
    print(cAlta)
    ### Comandos de creacion de los directorios dentro del home usuario
    if g == 'asir':
        lDir = lAsir.copy()
    elif g == 'daw':
        lDir = lDaw.copy()
    else:
        lDir =[]

    for d in lDir:
        cDirectorio = f'sudo mkdir /home/{conta}/{d.strip()}'
        cCambio = f'sudo chown {conta}:{g} /home/{conta}/{d.strip()}'
        cPermisos = f'sudo chown 0750 /home/{conta}/{d.strip()}'
        print(cDirectorio)
        print (cCambio)
        print(cPermisos)
        ## Ejecutamos los comandos
        call(cDirectorio, shell=True)
        call(cCambio, shell=True)
        call(cPermisos, shell=True)
    print(f'Damos de alta a: {conta}')
    print(150*'-')    
# print (cont)