from subprocess import run
from datetime import datetime

comando = run("top -bn1 -o %MEM",
              shell=True,
              capture_output=True,
              text=True).stdout
informe = "USER;COMMAND;%CPU;%MEM;PID;PPID\n"

for l in comando.split('\n')[7:]:
    ll = l.strip().split()
    mem = ll[9]
    if mem == '0,0':
        break
    else:
        print(ll)
        pid = ll[0]
        user=ll[1]
        command=ll[-1]
        cpu=ll[8]
        try:
            ppid = run(f"ps -f {pid}",
                  shell=True,
                  capture_output=True,
                  text=True).stdout.split('\n')[1].split()[2]
        except:
            ppid='null'        

        informe += f'{user};{command};{cpu};{mem};{pid};{ppid}\n'

agora = datetime.now().strftime("%Y_%m_%d_%H_%M)")

patharchivo = f'./top_{agora}.csv'

with open (patharchivo, "w", ) as csv:
    csv.write(informe)








