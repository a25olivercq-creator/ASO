# 1.- Lee accesos.log línea por línea.
# 2.- Usa un diccionario (dict) para contar cuántos intentos FAILED acumula cada usuario (str como clave, int como valor).
# 3.- Crea una lista (list) con los usuarios que hayan superado los 2 intentos fallidos (considerados sospechosos).

from os import path, remove

pathAcces = "./accesos.log"

dIntentosF = {}
lSos = []

if path.exists (pathAcces):

    with open(pathAcces) as  ac:
        lLineaAc = ac.readlines()

    for linea in lLineaAc:
        lLinea=linea.strip().split(",")
        # print(lLinea)
        l=(lLinea[2])
        usur=(lLinea[1])
        
        if l=="FAILED":
            # print(f"el usuario {usur} {l}")
            if usur not in dIntentosF:
                dIntentosF.setdefault(usur,1)

            else:
                dIntentosF[usur]=dIntentosF[usur]+1
        else:
            dIntentosF.setdefault(usur,0)  

    print (dIntentosF)    
    # Puedo sacar un informe con los datos extraidos y guardados en el diccionario
    for f,v in dIntentosF.items():
        if v>=4:
            lSos.append(f)
    else:
        pass

    print ("Los suarios con 4 o mas intentos fallidos son : ")
    print (f"{', '.join(lSos)}")

else:
    pass

