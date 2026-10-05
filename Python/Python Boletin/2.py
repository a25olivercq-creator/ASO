# 2.- El área A de un triángulo se puede calcular a partir del valor de dos de sus lados, a y b, y del ángulo ø que estos forman 
# entre sí con la fórmula: A = 1/2 * a * b * sin(ø). Diseña un programa que pida el valor de los dos lados (en metros), el valor 
# del ángulo que estos forman (en grados), y muestre el valor del área.
# [Ten en cuenta que la función sin de Python trabaja en radianes, así que el ángulo que se lea en grados hay que pasarlo a radianes 
# sabiendo que π radianes son 180 grados].

import math

# inicio mostrar titulo
print ("Programa que cálcula el el area de un triángulo: 25")
print ("#"*100)

# Leer datos de usuario
ladoa = float (input ("Introduce valor de lado A"))
ladob = float (input ("Introduce valor de lado B"))
angulo = float (input ("Introduce valor del ángulo"))

# Calculos
area = 1/2 * ladoa * ladob * math.sin(math.radians(angulo)) 

print (f"El area del triángulo es de {area:.2f}")