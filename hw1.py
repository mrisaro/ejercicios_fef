#%% Arranco con las librerías que uso
import numpy as np
import auxiliares as aux
import time

#%% Script
num_input = input('Insertar número: ')
num = int(num_input)

start_time = time.time()

nsq = int(np.sqrt(num)+1)
while not(num % nsq == 0 and aux.esPrimo(nsq)):
    nsq = nsq-1

elapsed_time = time.time() - start_time

testo = 'El mayor divisor primo es '+ str(nsq)
print(testo)
print(elapsed_time)
