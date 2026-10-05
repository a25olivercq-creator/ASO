# 1.- Realizar una función que devuelva una lista con una secuencia 
# Fibonacci hasta el número menor o igual a un número dado como parámetro.

# Se pide al usuario una cantidad... 100

n = int(input("Introduce un numero mayor que uno: "))
fibo = [0,1]

while True:
    resultado = fibo[-1] + fibo[-2]
    
    if fibo[-2] <= n: 
        fibo.append(resultado)
    else: break
    print (fibo)