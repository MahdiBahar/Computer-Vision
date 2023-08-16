# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:43:06 2023

@author: Mahdi Bahar

Solving the Exersice 12

Numpy
"""

#Exercise 1


import numpy as np

a = np.zeros((4,5,3))
print(a)

print(a.shape)

# Exercise 2




#Exercise 3

arr= np.array([[10,20,30,40],
               [50,60,70,80]
               ])

print(arr[1,0])


#Exercise 4

arr= np.array([[10,20,30,40],
               [50,60,70,80]
               ])
print(arr.dtype)

arr_changedtype= np.array([[10,20,30,40],
               [50,60,70,80]
               ],dtype=float)

print(arr_changedtype.dtype)