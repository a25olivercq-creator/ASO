# 1.- Calcular con un diccionario el tamaño total acumulado en MB (int) respaldado con éxito (OK) por cada servidor.
# 2.- Guardar en una lista de cadenas (str) las rutas/directorios cuyo respaldo haya dado estado FAILED.
# 3.- Genera un archivo de texto llamado resumen_ejecutivo.txt con un formato legible como este:

from os import path

dRes = {}
dfail ={}
lfails =[]

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
        t=int(t)

        if e=="OK":

            if s not in dRes:
                dRes.setdefault(s,t)
            
            else:
                dRes[s]+=t

        else:
            lfails.append(d)
            
            dfail.setdefault(s,e)

    print(dRes)
    print(lfails)
    print (dfail)

    with open("resumen_ejecutivo.txt", "w", encoding="utf-8") as archivo:
        archivo.write("=== RESUMEN DE RESPALDOS ===\n")
        archivo.write("Total MB respaldados por servidor (Solo OK):\n")
        for k,v in dRes.items():
            archivo.write(f"- {k} : {v} MB ({v/1024:.2f} GB)\n")
        archivo.write("\nRutas con fallos de respaldo (Atención requerida):\n")
        for k,v in dfail.items():
            archivo.write(f"* {k}: {v}\n")  
        else:
            pass
else:
    pass  