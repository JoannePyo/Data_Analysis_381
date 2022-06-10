from operator import index
import pandas as pd

#Extract these seven attributes from each line of the file and create seven distinct Python list objects comprised solely of the values 
#you extracted for a given attribute. 
h = ["price", "Maintenance cost", "Number of doors", "Number of passengers","Luggage capacity", "Safety rating", "Classification of vehicle"]
empty_price = []
empty_maintenanceCost = []
empty_numberOfDoors = []
empty_numberOfPassengers = []
empty_luggageCapacity = []
empty_safetyRating = []
empty_classificationOfVehicle = []
dataFrame = pd.read_csv("https://raw.githubusercontent.com/JoannePyo/Data_Analysis_381/main/HW/cars-sample35.xlsx%20-%20Worksheet.csv", names=h)

#list
empty_price = dataFrame["price"].tolist()
empty_maintenanceCost = dataFrame["Maintenance cost"].tolist()
empty_numberOfDoors = dataFrame["Number of doors"].tolist()
empty_numberOfPassengers = dataFrame["Number of passengers"].tolist()
empty_luggageCapacity = dataFrame["Luggage capacity"].tolist()
empty_safetyRating = dataFrame["Safety rating"].tolist()
empty_classificationOfVehicle = dataFrame["Classification of vehicle"].tolist()

#Find the list index values of each automobile having a “price” rating of "med". Create a new list object with your result. 
empty_list = []
index = 0
while index!=len(empty_price):
    if empty_price[index]== 'med':
        empty_list.append(index)
    index+=1
print(empty_list)

#Find the "number of passengers" value for each auto having a "price" value of "med". 
#Create a new list to store your findings and be sure to print your results.
empty_list2 = []
index = 0
while index != len(empty_price):
    if empty_price[index] == 'med':
        empty_list2.append(empty_numberOfPassengers[index])
    index +=1
print(empty_list2)

#Find the index value for each automobile having a “price” value of "high" 
#and a “maintenance” value that is not "low". Create a new list to store your findings and be sure to print your results.
empty_list3 =[]
index = 0
while index != len(empty_price):
    if empty_price[index] == 'high' and empty_maintenanceCost[index] != 'low':
        empty_list3.append(index)
    index +=1
print(empty_list3)


#Find the list index values of each automobile having a price rating of "med using a list comprehension instead of a basic for or while loop.  
#The list comprehension should create a new list containing your result. Be sure to print your results to the screen.
newListPrice= [index for index in range(len(empty_price)) if empty_price[index] == 'med']
print(newListPrice)

#Find the "number of passengers" value for each auto having a "price" value of "med" using a list comprehension instead of a basic for or while loop. 
#The list comprehension should create a new list containing your findings. Be sure to print your results to the screen.
newListNOP=[empty_numberOfPassengers[index] for index in range(len(empty_price)) if empty_price[index] == 'med']
print(newListNOP)


#Find the index value for each automobile having a price value of "high" and a maintenance value that is not "low" using a list comprehension. 
#The list comprehension should create a new list containing your findings. Be sure to print your results to the screen.
newList = [index for index in range(len(empty_price)) if empty_price[index] == 'high' and empty_maintenanceCost[index] != 'low']
print(newList)

#Extract each individual element of the component lists contained within nlist and add them to a new list.  
#Do NOT use a nested for loop, use a list comprehension.
#List Comprehensions: [expr for val in collection] || [expr for val in collection if <text>]

nlist = [ [1, 2, 3], ['A', 'B', 'C'], [4, 5], ['D', 'E'] ]
listComp=[y for x in nlist for y in x]
print(listComp)

