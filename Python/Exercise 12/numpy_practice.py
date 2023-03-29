# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:47:32 2023

@author: Mahdi Bahar

prictice numpy
"""

import numpy as np

arr = np.array([1,2,3])

print(arr)

print(type(arr))

# dimention of array
print(arr.ndim)


#data type elements of array

print(arr.dtype)
## all of the elements should be the same

#float array

arr_float = np.array([1,2,3],dtype=np.float64)
print(arr_float.dtype)

#array 2D
arr_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2D.ndim)
print(arr_2D)

print(arr_2D[1,1])

# array 3D
arr_3D = np.array([
    [
    [1,2,3],
    [4,5,6]
                    ],
    [
    [7,8,9],
    [11,12,13]
    ]
                   ])

print(arr_3D)
print(arr_3D.ndim)


# shapes
print(arr.shape)
print(arr_2D.shape)
print(arr_3D.shape)