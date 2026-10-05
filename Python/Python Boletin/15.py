

while True:
    n=int(input("Dame un numero (0 para salir): "))
    try:
        esPrimo = True 
        for i in range (2,n):
            resto = n % i
            if resto == 0: 
                esPrimo=False
                break
            else:
                pass
        if esPrimo:
            print (f"El numero {n} SI es primo")
        else:
            print (f"El numero {n} NO es primo")
    except:
        print("Introduce numero valido")