'''NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.'''

import numpy as np

a = np.array(42) # 0-D Array
b = np.array([1, 2, 3, 4, 5]) # 1-D Array


c = np.array([                # 2-D Array
    [1, 2, 3], [4, 5, 6]
    ])
#Above can be written as: 
# c = np.array([[1, 2, 3], [4, 5, 6]])           # 2-D Array

d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
    ])
#Above can be written as: 
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)