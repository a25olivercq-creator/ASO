from subprocess import run, call
from datetime import datetime

comando = run("top -bn1 -o %MEM",
              shell=True,
              capture_output=True,
              text=True).stdout.splitlines()[6:]

# print(comando.stdout)

print ("\n".join(comando2))

# with open(f"top_{datetime()}.csv","w",encoding='utf-8') as csv:
#     csv.write(comando.stdout)

