# Compresor simple: Escribe un programa que tome una cadena
# de texto formada por letras repetidas consecutivas
# y las comprima contando las repeticiones consecutivas usando
# bucles y listas.

# - Ejemplo de entrada: AABCCCDEEOOOZZRTTLL
# - Ejemplo de salida: 2A1B3C1D2E4O2Z1R3T2L

texto= input("Escribe un texto : ")

contador= 0
codigo = ''
letra = ''

for c in texto:
    if c == letra:
        contador +=1
    else:
        codigo = codigo +str(contador)+letra
        letra=c
        contador = 1
codigo = codigo + str(contador) + letra
codigo = codigo[1:] 
print (codigo)
      