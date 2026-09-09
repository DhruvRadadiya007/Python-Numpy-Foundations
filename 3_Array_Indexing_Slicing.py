import numpy as np

print(" Basic indexing ")

arr = np.array([1,2,3,4,5,6])

print(arr[0])
print(arr[-1])

print("\n")
print(" Basic slicing ")
print("\n")

print(arr[1:3])
print(arr[:5])
print(arr[::2])
print(arr[::-1])

print("\n")
print(" 2d indexing and slicing ")
print("\n")
arr1 = np.array([[1,2,3,4,],
                 [5,6,7,8]])

print(arr1[0,2]) # row 0 and column 2
print(arr1[:,2]) # all rows ans column 2
print(arr1[0,:]) # row 0 and all columns

print(arr1[0:2,1:3]) # rows 0 TO 2 and columns 1 to 3 creates sub-matrix

print("\n")
print(" Boolean indexing")
print("\n")

print(" 1D array ")
arr = np.array([10,20,30,40,50])

mask = arr > 25 # stores bool values based on condition
print(mask)

print(arr[mask]) # prints the array values not bool values

print("using short trick :")
print(arr[arr>25])
print([arr>25])

print()
print(" 2d array :")

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr2[arr2%2 == 0]) # prints all the even numbers in a 1d array
print([arr2%2 == 0]) # prints all the even values in the form of bool

print("\n")
print("Fancy indexing ")
print("\n")

print(" 1d array ")

a = np.array([10,20,30,40,50,60,77]) # creating an array 
index = np.array([1,4,6]) # taking the index value to be printed
print(a[index]) # prints the index value of the array

print()
print(" 2d array ")
b = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 2d array
rows = np.array([0,2]) # selecting the rows 0 and 2
print(b[rows]) # prints the rows


print("\n")
print("shared memory and views")
print("\n")

m = np.arange(1,10).reshape(3,3) # reshape helps to create matrix of an array

print("matrix = ",m)

sub = m[0:2,1:3] # this creates a shared memory from the main matrix
print("sub matrix = ",sub)
sub[0,0] = 99 # this will also change the element in the main matrix
print(m) 

print("creating an independent array without shared memory")

sub_copy = m[0:2,1:3].copy() # use copy function
sub_copy[0,0] = 77 # this will not change the main matrix 
print(sub_copy)
