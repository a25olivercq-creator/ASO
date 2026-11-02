
#Funcion que dado como parametro un archivo me devuelve un diccionario

def fileToDict(pathFile):

    dFile={}
    try:
        with open(pathFile) as fr:
            lFile = fr.readlines()

        for l in lFile:
            if l.strip() !='':  #Eliminamos las lineas en blanco
                ll=l.strip().split(':') #Dividimos las lineas en dos campos
                k=ll[0].strip() #La clave es el primer campo
                v=ll[1].strip()
                if v == '':
                    v = None
                else:
                    pass
                dFile.setdefault(k,v)
            else:
                pass
    except:
        pass

    return dFile        #La funcion devuelve el diccionario con todo el contenido

def fInfoCPU():
    
    dInfoCPU=(fileToDict('/proc/cpuinfo'))

    dCPUinfo = {}

    dCPUinfo.setdefault('modeloCPU', dInfoCPU['model name'])
    dCPUinfo.setdefault('familiaCPU',dInfoCPU['cpu family'])
    dCPUinfo.setdefault('frecuenciaCPU',dInfoCPU['cpu MHz'])
    dCPUinfo.setdefault('coresCPU',dInfoCPU['cpu cores'])
    dCPUinfo.setdefault('flags',dInfoCPU['flags'].split())

    print(dCPUinfo)