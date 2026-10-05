# 1.- Hacer un programa que pida el radio por pantalla y devuelva el perímetro, el área y el volumen utilizando dicho parámetro:
# Nota: En la resolución de este problema se utiliza el módulo math.

# import math 
from math import pi, pow

# Inicio mostrar titulo
print ("Progama que calcula perímetro, área y volumen")
print ("#"*50)

try:
    # Leer datos de usuario
    radio = float (input ("Introduce radio: ").replace(',','.'))
    print (type (radio))

    # TODO:Cálculo del perímetro

    perimetro = 2* pi * radio
    area = pi * pow(radio,2)
    volumen = 4 * pi * pow(radio,3)

    # Mostrar resultados por pantalla
    print ("-"*50)
    print (f"\nEl radio introducido es {radio}")
    print (f"El perimetro de un aro de radio {perimetro:.2f} cm")
    print (f"El area de una circunferencia de radio {radio:.2f} cm es {area:.2f} cm²")
    print (f"El volument de una circunferencia de radio {radio:.2f} cm es {volumen:.2f} cm³")

except:
    print ("introduce radio valido")
