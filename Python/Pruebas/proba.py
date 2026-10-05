print ("Programa que comprueba si un numero es par o impar")
print ("#"*100)

while True:
    num = int (input("Introduce numero: "))

    resto = num % 2 

    print (f"El número {num} dividido por 2 tiene resto {resto}")


    if resto == 0:
        break
    else :
        print (f"El número {num} es impar")
