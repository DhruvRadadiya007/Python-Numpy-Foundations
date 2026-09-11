import numpy as np
print("\n")
print(" Reshaping ")
print("\n")
a = np.arange(6)
print(a) # not arranged
reshaped = a.reshape(2,3) # creates a multi dimensional array from a 1d array
print(reshaped) # arranged
# shortcut :- a = np.arange(6).reshape(2,3)

print("\n")
print(" Flattening ")
print("\n")

flat = reshaped.flatten()
print(flat) # this create a 1d array of a matrix

print("\n")
print(" Stacking ")
print("\n")

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
 
print(np.hstack((a,b))) # this wil stack the array horizontally 
print(np.vstack((a,b))) # this will stack the array vertically

