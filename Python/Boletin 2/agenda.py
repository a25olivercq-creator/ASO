pathAchAg = "./agenda.txt"

dAgenda = {}
from os import path, remove

if path.exists(pathAchAg):

    from subprocess import run

    with open(pathAchAg) as fr:
        lLineasAr = fr.readlines()

    for linea in lLineasAr:
        lLinea=linea.split(":")
        if len(lLinea) == 2: #Me quedo con las lineas que tienen clave y valor
            # print(lLinea)
            # print(lLinea[0])
            # print(lLinea[1].strip())
            c = lLinea[0]
            t = lLinea[1].strip()
            dAgenda.setdefault(c,t)
        else:
            pass

else:
    pass

print(dAgenda)

while True:
    run ("clear")
    c = input("Contacto : (* para salir y ver toda la agenda)  ")

    if c != '*':

        if c in dAgenda:
            print (f"El contacto {c} tiene el numero {dAgenda[c]}")
            print("""

                Para modificar el telefono del contacto, pulse 1.

                Para eliminarlo, pulse 2.

                Enter para continuar.
            
            """)
            opt = input("Opcion: ")

            if opt == "1":
                n2 = input("Introduzca el nuevo número :")
                dAgenda[c]=n2
                
            elif opt == "2":
                s = input("Pulse 's' para confirmar :")
                if s == "s":
                    dAgenda.pop(c)
                    print ("El contacto ha sido eliminado")

                else:
                    pass
                
            else:
                pass

            print(dAgenda)
            input("\n pulsa cualquier tecla para continuar")
                
        else:
            n = input("Numero : ")
            dAgenda.setdefault(c,n)
            print (dAgenda)
            input("\n pulsa cualquier tecla para continuar")

    else:
        break
# print(dAgenda)
# Re-escribimos el contenido del archivo agenda.txt con el diccionario
# ####### Primera opcion de solucin con 'w' todo a un string y escribirlo una sola vez

# sAgenda= ""
# for k,v in dAgenda.items():
#     print(f"{k}:{v}")
#     sAgenda += f"{k}:{v}\n"
# print(sAgenda) 

# # Vamos a guardar sAgenda en un archivo llamado ./agenda2.txt
# pathArchAg2= "./agenda2.txt"
# with open(pathArchAg2,"w") as fw:
#     fw.write(sAgenda)


#  ###### Segunda opcion de solucion con 'a' (append) al archivo, elemento a elemento desde el diccionario

# pathArchAg2= "./agenda2.txt"
if path.exists(pathAchAg): #Si el archivo de salida existe la borramos porque vamos a guardar 'TODA' la agenda de nuevo
    remove(pathAchAg)

#Abrimos el archivo en modo 'append' (si no existe lo crea en vacio y añadimos elemento a elemento)

with open(pathAchAg,'a') as fa:
    for c,t in dAgenda.items():
        fa.write(f"{c}:{t}\n")


