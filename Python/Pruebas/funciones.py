#Funciones deifinidas por el usuario

def muestraSaludo(saludo):
    print(" - "*20)
    print(f'\t{saludo}')
    print("-"*20)

# Texto = "Hola"
# muestraSaludo(Texto)

# listaSaludos = ["Hola", "Adios" , "Buenas", "Ciao"]
# for saludos in listaSaludos:
#         muestraSaludo(listaSaludos) 

def factorial(n):
    f=1
    for a in range (1,n+1):
        f*=a
    return f

# numero = 7
# print (factorial(numero))

# numeros = [7,45,55,2,8]

#Funcion que, dado un numero, devuelve True o False si
# es o no es primo

def primo(n):
    esPrimo = True 
    for i in range (2,n):
        resto = n % i
        if resto == 0: 
            esPrimo=False
        break
    else:
        pass

    return esPrimo




