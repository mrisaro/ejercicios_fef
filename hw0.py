#%% Prueba de tarea_0
"""
Los números menores a 10 que son múltiplos de 3 o 5 son 3, 5, 6 y 9.

La suma de estos números es 23.

Calculá la suma de todos los múltiplos de 3 o 5 menores a 1000
"""

#%% Arranco con el Script
num_input = 1000

s = 0

for ii in range(1,num_input):
    if ii % 3 == 0 or ii % 5 == 0:
        s = s + ii

testo = 'La suma da : ' + str(s)
print(testo)
