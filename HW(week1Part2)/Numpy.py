#problem 1
#load the numpy library into your python environment
import numpy as np

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
#the distinct overlapping values
overloap = np.intersect1d(a,b)

#printout overlapping values
print("problem 1 answer: ", overloap)
print()

#problem 2
#make 5x3 array
matrixArray = np.array([ [1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15] ])
print("problem 2 answer: \n", matrixArray.T)
print()

#problem 3
#flattening 
flattening = matrixArray.flatten()  # we can use matrixArray.revel() or matrixArray.reshape(-1)
print("problem 3 answer: \n", flattening)
print()

#problem 4
#Transform the 2-D array shown in Problem 2 into a 3 dimensional array such 
#that the first column becomes the first dimension of the 3-D array, 
#the second column becomes the second dimension of the 3-D array, 
#and the third column becomes the third dimension of the 3-D array. 

transform= matrixArray.reshape(3, 5, 1) 
print("problem 4 answer: \n", transform)  
print()

#problem 5
#transform the 3-D array you created in Problem 4 back to the 2-dimensional format shown in Problem 2.
print("problem 5 answer: \n" , transform.T)
print()

#problem 6
#list of arrays
a = np.array([12, 5, 7, 15, 3, 1, 8])
b = np.array([14, 6, 3, 11, 19, 12, 5])

#remove duplication numbers
for x, val in enumerate(a):
    if val in b:
        a = np.delete(a, np.where(a == val)[0][0])
        b = np.delete(b, np.where(b == val)[0][0])

for y, val in enumerate(b):
    if val in a:
        a = np.delete(a, np.where(a == val)[0][0])
        b = np.delete(b, np.where(b == val)[0][0])
        
#concatenate two numbers        
c = np.concatenate((a, b))

#make sort
c.sort()
#print out unique numbers
print("problem 6 answer: \n" , c)
print()

#problem 7
import pandas as pd