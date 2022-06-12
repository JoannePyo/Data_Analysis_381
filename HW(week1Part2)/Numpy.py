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
##load the pandas library into your python environment
import pandas as pd

dataFrame = pd.read_csv("https://raw.githubusercontent.com/JoannePyo/Data_Analysis_381/main/HW(week1Part2)/Module6_Data.csv.csv")
dataFrame

#7-1. What is the maximum yearly NYC consumption of water in millions of gallons per day?

#numpy array
year = dataFrame["Year"].values
NYC_population  = dataFrame["New York City Population"].values
NYC_consumption = dataFrame["NYC Consumption(Million gallons per day)"].values
per_Capita = dataFrame["Per Capita(Gallons per person per day)"].values

#use np.max to find out maximum number.
max_yearly = np.max(NYC_consumption)
print("Problem 7-1. Maximum Yearly NYC Consumption:", max_yearly, "millions of gallons per day")
print()

#7-2. How many calendar years are represented within this data set? 
#     NumPy's shape command is one way to find out.
print("Problem 7-2.", Year.shape, "calendar years")
print()

#7-3. What is the mean and the standard deviation of the per capita daily water consumption?
#find the mean
mean = np.average(per_Capita)
print(f"Problem 7-3. The mean of per capita daily water consumption is {mean: .2f}")

#find the standard deviation
Standard_deviation = np.std(per_Capita)
print(f"Problem 7-3. The standard deviation of the per capita daily water consumption is {Standard_deviation: .2f}")
print()

#7-4. What is the increase or decrease in population from year to year? 
#     Use NumPy's `diff` function to create an array of differences and save that 
#     to a variable called "pop_diff", then print that variable to the screen.

#find out the different
population_different = np.diff(NYC_population)
print("Problem 7-4. The increase or decrrease in pupulation from year to year: \n", population_different)
