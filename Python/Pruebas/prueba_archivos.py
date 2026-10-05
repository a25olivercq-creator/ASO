# Trabajo con archivos

pathArchivo ='./cpuinfo'
with open(pathArchivo) as fr:
    # Trabajo con el archivo
    lineasArchivo= fr.readlines()
    print(lineasArchivo)