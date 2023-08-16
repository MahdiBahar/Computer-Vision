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


######
#zero array
arr_zero = np.zeros((2,3),dtype= np.int32)
print(arr_zero)

#####
# one array
arr_one = np.ones((2,3,4),dtype= np.int32)
print(arr_one)

#arange

a = np.arange(1, 10,2)
print(a)

#linspace
b= np.linspace(1,2,5)
print(b)


#indexing

arr_id = np.arange(1,9)
print(arr_id)
print(type(arr_id))

print(arr_id[4])

## 2D
arr_2d = np.array([
    
    [1,2,3],
    [4,5,6]
    
    ])

print(arr_2d.shape)
print(arr_2d[0])
print(arr_2d[1,1])

## 3D

arr_3d = np.array([
    [
     [1,2],[3,4],[5,6]
     ],
    [
     [7,8],[9,10],[11,12]
     ]
    ])

print(arr_3d.shape)
print(arr_3d[1,2,0])

## slicing

#2D
arr_2d_slciing = arr_2d[:1,1:]
print(arr_2d_slciing)


## View , Copy

a= np.array(
    [[80,81,82],
    [83,84,85]
    ]
    )
b=a[0:,0:2]
c=a[0:,0:2].copy()

c[0,0]=0

print(b)

print(c)

print(a)

### np.add
### np.subtract
### np.multiply
### np.divide