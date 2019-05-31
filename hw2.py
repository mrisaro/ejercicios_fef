#%% Importar librerías

import numpy as np
import matplotlib.pyplot as plt
import auxiliares as aux

#%% Arranco ahora a calcular los elementos de series

n_max = int(1e6)
l_col = np.zeros((n_max,1))
expo = 1e5

for i in range(1,n_max):
    l_col [i] = aux.len_collatz(i)
    if i % expo == 0:
        print(i)

[ind_max,len_max] = [np.argmax(l_col), np.max(l_col)]
testo = 'La sucesión más larga de Collatz incia con ' + str(ind_max)

#%% Paso ahora a graficar un poco

my_dpi = 96
plt.figure(1,figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)
plt.plot(np.arange(n_max),l_col)
plt.xlabel('Entero inicio', fontsize = 14)
plt.ylabel('Largo serie', fontsize = 14)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.grid(linestyle='--')
plt.tight_layout()

plt.show()
