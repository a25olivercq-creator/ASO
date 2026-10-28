from subprocess import run

# { 	‘nombre’ : ‘’,
# 	‘so’ : ‘’,
# 	‘kernel’ : ‘’,
# 	‘arquitectura’ : ‘’,
# 	‘bios’ : {	‘fabricanteBios’ : ‘’,
# 				‘versionBios’ : ‘’,
# 				‘fechaBios’ : ‘’,
# 				‘revisionBios’ : ‘’}, 

dIS = {}          #dInfoSistema

nombre = run('hostname', 
                shell=True,
                capture_output=True,
                text=True,
                encoding="utf-8").stdout

dIS.setdefault('nombre',nombre)

print(dIS)