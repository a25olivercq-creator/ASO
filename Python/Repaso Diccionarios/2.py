# 1.- Calcular con un diccionario el tamaño total acumulado en MB (int) respaldado con éxito (OK) por cada servidor.
# 2.- Guardar en una lista de cadenas (str) las rutas/directorios cuyo respaldo haya dado estado FAILED.
# 3.- Genera un archivo de texto llamado resumen_ejecutivo.txt con un formato legible como este:

dRes = {}
from os import path

PathCSV = "./reporte_backups.csv"

if path.exists (PathCSV):
    with open(PathCSV) as csv:
        lLineaCSV = csv.readlines()
    for linea in lLineaCSV[1:]:
        lLinea=linea.strip().split(",")
        s=lLinea[0]
        d=lLinea[1]
        t=lLinea[2]
        e=lLinea[3]

        if e=="OK":

            if s not in dRes:
                dRes.setdefault(s,t)
            
            else:
                dRes[t]+t

        else:
            dRes.setdefault(s,0)
    print(dRes)

    print(lLinea)
