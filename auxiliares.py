#%% Script donde almaceno todas las funciones que utilizo para las hw
import numpy as np

#%% Funciones para tarea de primos

def esPrimo(n):
    noEsPrimo = False
    for i in range(2,int(np.sqrt(n))+1):
        if n % i ==0:
            noEsPrimo = True
            break
    esPrimo = not noEsPrimo
    return esPrimo

#%% Funciones para tarea de sigCollatz
# funcion para calcular siguiente elemento de Collatz
def sigCollatz(n):
    if n % 2 == 0:
        sc = n/2
    else:
        sc = 3*n+1

    return sc

# funcion para calcular longitud sucesión de Collatz
def len_collatz(n):
    suce = [n]
    while n != 1:
        n = sigCollatz(n)
        suce.append(n)

    return len(suce)
