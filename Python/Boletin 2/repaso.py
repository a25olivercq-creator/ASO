
listentrada=[12,-5,0,8,-2,7,14,-5,3]
listasalida=[]
suma = 0

for n in listentrada:
    if (n>0) and (n%2 == 0):
        listasalida.append(n)
        suma = sum(listasalida)

print (f"Lista de entrada: {listentrada}")
print (f"Lista de salida: {listasalida}")
print (f"Suma: {suma}")