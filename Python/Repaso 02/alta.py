import unicodedata
def eliminaTildes(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

from subprocess import run, call

pathU='./Usuarios.csv'

with open (pathU, 'r', encoding='utf-8') as fr:
    lUsuarios=fr.readlines()

for l in lUsuarios[1:]:
    ll=l.strip().split(";")
    print(ll)
    ano=ll[7].split('/')[2]
    conta =f"a27{ll[2]}{ll[0][0]}{ll[1][0]}{ano}"
    print(conta)

    if ll[5] == 'DNI':
        password = run(f'openssl passwd -6 {ll[6]}',
                    shell=True,
                    capture_output=True,
                    text=True,
                    encoding="utf-8").stdout.strip()
    else:
        password = run('openssl passwd -6 abc123..',
                    shell=True,
                    capture_output=True,
                    text=True,
                    encoding="utf-8").stdout.strip()

    print(password)

    if ll[5] == 'ASIR':
        g = 'galumasir'
    elif ll[5] == 'DAW':
        g = 'galumdaw'
    else:
        g='galum'

    gsecjef=run('groups jefe',
                shell=True,
                capture_output=True,
                text=True,
                encoding="utf-8").stdout.strip().split()

    gsec = gsecjef[3:]
    print(gsec)
    call(f"useradd -d /home/{conta} -m -g {g} -G galum,gies,{",".join(gsec)} -s /bin/bash -p '{password}' {conta} ", shell=True)
    
    
    print('-'*50)
