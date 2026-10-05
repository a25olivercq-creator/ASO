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


dAgenda ={}

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

