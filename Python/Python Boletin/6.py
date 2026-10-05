# 6.- Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

# Creamos una lista vacia para guardar los números
lnum = []
while True: #rellenamos la lista de numeros
    # Le pedimos al usuario que nos de un número
    n = int(input('Dame un número (0 para salir): '))
    # Añadimos el numero a la lista
    if n== 0:
        break
    else:
        lnum.append(n) 

    print (lnum)

    suma = sum(lnum)
    media = suma/len(lnum)

    print ("#"*100)
    print (f"La suma de los números es : {suma}")
    print (f"La media de los números es : {media}")