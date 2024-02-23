'''
Create a NumPy ndarray Object
NumPy is used to work with arrays. The array object in NumPy is called ndarray.

We can create a NumPy ndarray object by using the array() function.

'''
import numpy as np

# Immutable since it is tuple 
arr_tuple = np.array((1,2,3,4,5)) 
print(arr_tuple)

# Mutable since it is list
arr_list = np.array([1,2,3,4,5])
print(arr_list)
