# 1. - Abrir el archivo /etc/passwd ... convertirlo en una lista

from subprocess import run

with open('/etc/passwd') as fr:
    lPasswd = fr.readlines()

for l in lPasswd:
    ll = l.strip().split(':')
    # print(ll)
    conta = ll[0]
    print(conta)


# cPasswd = run('cat /etc/passwd',
            #   shell=True,
            #   capture_output=True,
            #   )
