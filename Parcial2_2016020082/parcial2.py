##Se empieza importando la libreria a utilizar, en este caso usaremos NumPy para las operaciones matematicas

import numpy as np
import time


dataset = np.random.normal(loc = 500, scale = 30, size = 10000000)

inicio = time.time()

data_array = np.array(dataset)
remaining_data = data_array[data_array < 500000 ]
remaining_data = np.sum(remaining_data)

print ('La suma total de los datos que quedan es: ',remaining_data)
print ('Ha durado una cantidad de: {} segundos'.format(time.time() - inicio ))


