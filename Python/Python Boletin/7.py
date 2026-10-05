# 7.- Crea una aplicación que permita adivinar un número generado aleatoriamente entre el 1 y el 100. El programa va pidiendo números y 
# va respondiendo si el número a adivinar es mayor o menor que el introducido. 
# El programa termina cuando se acierta el número.
# y devuelve al jugador: "Acertaste en X intentos"

import random
import subprocess

subprocess.call ('clear', shell=True)
numero = random.randint(1,100)
cont = 0
# print (numero)
while True:
    n = int(input("Adivina un número del 1-100 : "))
    subprocess.call ('clear', shell=True)
    cont+=1

    if numero>n:
        print ("El numero a adiviar es mayor que el introducido")
    elif numero<n:
        print ("El numero a adiviar es menor que el introducido")
    elif numero == n:
        print (f"Acertaste en {cont} intentos")
        break






