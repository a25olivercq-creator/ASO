#Programa que pida un numero y calcula su factorial
#Factorial de un numero 5=5*4*3*2=120
#Siga pidiendo numeros hasta que el usuario pone un 0
#Tenga ontol de errores si no se introduce un numero

print ("Programa que calcula el factorial")

while True:
    try:

        n = int((input("Dame un numero (0 para salir): ")))
        if n!=0:
        #CAlculamos el factorial y mostramos
            f=1
            for a in range (1,n+1):
                f*=a
                print (f)
        else:
            break
    except:
        print ("Introduce un numero valido")