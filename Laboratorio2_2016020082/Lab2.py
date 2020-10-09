
import numpy as np
import time

container = np.random.normal(500,30,10000000)

inicio = time.time()
estruct = []
for var in container:
    if (var <= 5000000):
        estruct.append(var)

print("Suma de los menores de 5000000", sum(estruct))
print('La duracion fue de: {} segundos'.format(time.time() - inicio))