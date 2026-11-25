import numpy as np

#creating one D array 
arr1 = np.array([1,2,3])
print('arr1:',arr1)
print()

#printing 2 d array
arr2 = np.array([[1,2,3],[4,5,6]])
print('arr2:' ,arr2)
print()

#list operations in numpy 
lst = [1,2,3] 
print('multiplied_list:', lst*3) #will multiply the same list thrice
print()

lst2= [1,2,3]
lst3= [4,5,6]
print('lst1+lst2:', lst2+lst3) #list addition
print()

arr3 = np.array([3,4,5])
print('arr3:' ,(arr3*2))
print()

zeros = np.zeros((2,3))
print('zeros:',zeros)
print()

ones = np.ones((2,3))
print('ones:',ones)
print()

full = np.full((4,4),7)
print('full:',full)
print()

from typing import Sequence
Sequence = np.arange(0,12,2)
print('sequence:', Sequence)
print()

random = np.random.random((4,4)) #any random values from 0 to 1
print('random',random)
print()

vector = np.array([1,2,3])
print(vector)#oneD array is a vector
print()

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('/nmatrix:', matrix) #matrix is a 2d array


tensor = np.array([[[1,2],[3,4],[5,6]],
                  [[1,2],[3,4],[5,6]]])
print('\ntesnsor:', tensor)
print('\ntensorshape:',tensor.shape)  #tensor is n/multiple dimentional array
arr = np.array ([[1,2,3],
                 [3,4,5]])
print("\nshape=", arr.shape) # shape as in rows into cols
print('\ndimension=s' , arr.ndim) #ndim is a method to get dimensions 
print('\nsize:',arr.size) #total number of elements in array
print('\ndtype:',arr.dtype) #data type of elements


arr = np.arange(12) # from 0 to 1 no increment given
print('\noriginal array:' , arr)
reshaped = arr.reshape((3,4))
print('\nreshaped array :' , reshaped)

flatten = reshaped.flatten()
print('\nflatten',flatten) # will flatten the reshaped array

raveled= reshaped.ravel()
print('\nravel:',raveled)# will return view instead of copy


 # .T is method that performs transpose operations on matrix
transpose = reshaped.T
print('/ntranspose:', transpose)

#Slicing:
arr = np.array ([1,2,3,4,5,6,7,8,9,10])
print('\nbasic slicing:', arr[2:7])
print('\nwith step',arr[2:9:3])
print('\nnegative indexing:', arr[-3])

arr_2d =np.array ([[1,2,3],
           [4,5,6],
           [7,8,9]])
print('\nspecific element', arr_2d[2,2])
print('\nspecific row:' , arr_2d[2])
print('\nentirecol:', arr_2d[:,2])





