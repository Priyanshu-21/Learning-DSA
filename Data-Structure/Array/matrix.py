import numpy as np
a = [[2, 0, 0, 0], [0, 3, 0, 0], [0, 0, 4, 4], [0, 0, 5, 5]]
b = np.array(a, dtype= np.float32)

b[2] = b[2] - b[2, 1] * b[1] 

print(b[2])