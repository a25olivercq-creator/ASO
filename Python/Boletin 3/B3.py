# from subprocess import run
# from platform import system
# # { 	‘nombre’ : ‘’,
# # 	‘so’ : ‘’,
# # 	‘kernel’ : ‘’,
# # 	‘arquitectura’ : ‘’,
# # 	‘bios’ : {	‘fabricanteBios’ : ‘’,
# # 				‘versionBios’ : ‘’,
# # 				‘fechaBios’ : ‘’,
# # 				‘revisionBios’ : ‘’}, 

# dIS = {}          #dInfoSistema

# nombre = run('hostname', 
#                 shell=True,
#                 capture_output=True,
#                 text=True,
#                 encoding="utf-8").stdout

# dIS.setdefault('nombre',nombre)

# so = system()

# dIS.setdefault('so',so)

# print(dIS)

# for clave, valor in dIS.items():
#     print(f'{clave}:{valor}\n')

from misFunciones import fileToDict

dInfoCPU=(fileToDict('/proc/cpuinfo'))

dCPUinfo = {}

dCPUinfo.setdefault('modeloCPU', dInfoCPU['model name'])
dCPUinfo.setdefault('familiaCPU',dInfoCPU['cpu family'])
dCPUinfo.setdefault('frecuenciaCPU',dInfoCPU['cpu MHz'])
dCPUinfo.setdefault('coresCPU',dInfoCPU['cpu cores'])
dCPUinfo.setdefault('flags',dInfoCPU['flags'].split())

print(dCPUinfo)


