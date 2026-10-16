
from subprocess import call, run
from re import compile,search, compile, findall 

# directorio = input("Dame nombre carpeta: ")

# # comando = ['mkdir', './carpeta']
# comando = f"mkdir {directorio}"

# call(comando, shell=True)



comando="ip addr"
ejeComando = run(
    comando,
    shell=True,
    capture_output=True,
    text=True,
    encoding='utf-8',
    check=True
)

salidaComando= ejeComando.stdout.strip()

##### Dado un texto, comprobar si en ese string hay simbolos:
##### Espacios, puntuación... ' \W' lo contrario de '\w' = [a-z0-9]

# nombreUsuario = "pepe55?"

# patronSimbolo = compile(r'\W')

# #Comprobando si ese patron aparece en el texto
# if print(patronSimbolo.search(nombreUsuario)):
#     print("Nombre usuario NO valido")
# else:
#     print("Nombre usuario SI es valido")



# texto = "pepe55"
# patronNumero=compile(r'[0-9]')
# numeros = patronNumero.findall(texto)
# print(numeros)

print(salidaComando)
print('-'*100)

patronIP = compile(r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}')
patronMAC = compile(r'(?:[0-9A-F]{2}[:-]){5}[0-9A-f]{2}')
listaIPs = patronIP.findall(salidaComando)
listaMACs=patronMAC.findall(salidaComando)
print(listaIPs)
print(listaMACs)