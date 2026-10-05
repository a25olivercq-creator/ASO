# Pide al usuario una frase por teclado. 
# Utilizando el bucle for e inspeccioando cada caracter
# de la cadena de tecto, cuenta cuantas vocales y 
# cuantas consonantes tiene 
# (ignora espacios, numeros y signos de puntiacion):

# Ejemplo: "Python 3.12 es genial"
# Salida: 
    # -Vocales:5
# -Consonantes: 9 

texto = input("Introduce un texto : ")
vocales = 0
consonantes = 0
expepciones = {65,69,73,79,85}

for c in texto.upper():
    codigo = ord(c)
    if codigo in expepciones:
        vocales+=1
    elif codigo in range(65,91) and codigo not in expepciones:
        consonantes+=1
    else: 
        pass

print (f"Vocales  : {vocales}")
print (f"Consonantes  : {consonantes}")