# Escribir un programa que vaya solicitando al usuario que ingrese nombres.
# a) Si el nombre se encuentra en la agenda (implementada con un diccionario),
# debe mostrar el teléfono y, opcionalmente,
# permitir modificarlo si no es correcto y eliminar el contacto.
# b) Si el nombre no se encuentra,
# debe permitir ingresar el teléfono correspondiente.
# El usuario puede utilizar la cadena "*", para salir del programa.


# "manuel" ; "987987987"

# Definimos variable diccionario para guardar toda la agenda

from subprocess import run

dAgenda={}

while True:
    
    run ("clear")
    c = input("Introduce el nombre del contacto (* para salir) : ")
    if c!="*":
        if c in dAgenda:
            print (f"El tlf de {c} es {dAgenda[c]}")
            print (
                """
                Elige opción:
                    1.-Modifical teléfono
                    2.-Eliminar teléfono
                    Otro.- Continuar
            """
            )
            opt = input("Opcion : ")
            if opt == 1:
                n2=input("Introduzca el nuevo numero : ")
                dAgenda[c] = n2
                print(dAgenda)
            elif opt == 2:
                eli=input("¿Seguro quieres eliminar? (Pulsa 's')")
                if eli.lower()=='s':
                    dAgenda.pop(c)
                    print (f"El contacto {c} fue eliminado")
                print(dAgenda)
            else:
                pass
        else:
            n = input ("Introduce el numero del contacto : ")
            dAgenda.setdefault(c,n)
            print (dAgenda)
            input ("\nPulsa una tecla para continuar")
            
    else:
        break