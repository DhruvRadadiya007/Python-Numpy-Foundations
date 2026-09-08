import numpy as np

print("creating a 1d array\n")  
arr1 = np.array([1, 2, 3])
print(arr1)
print(arr1.shape) # function used to find the shape of the array(columns,rows)

print("creating a 2d array\n")

arr1 = np.array([[1,2,3,4],
                [1,2,3,4]])
print(arr1)
print(arr1.shape)

print("\n")
arr = np.array([1,2.5,3,4])
print("data type :- ",arr.dtype) # numpy automatically converts data types

print("# making a array of tuple\n")
arr = np.array((1,2,3,4))
print(type(arr)) 
 

print("# making an array of zeros\n")

a=np.zeros((2,3) , dtype= float) # we can also give a data type
print(a)

print("# making an array of ones\n")

a=np.ones((2,3) , dtype= float) # we can also give a data type
print(a)

print("# making an array of a specific value\n")

a=np.full((3,3) ,7) # we can give a number
print(a)

print("# making an array with diagonals 1 and 0 elsewhere\n")

a = np.eye(3) # this creates squared matrix
print(a) 

a = np.eye(3,4) # this creates non - squared matrix
print(a) 

a = np.eye(4, k=1) # k is used to shift position of the diagonal
print(a)

print("# making an array with range function\n")

a= np.arange(0,10,2) # here the array is created by giving (start,end,step)
print(a)
a = np.linspace(0,1,5) # here the evenly spaced array is created by giving (start,end,number of even values you want )
value,step = np.linspace(0,1,5, retstep=True) # retstep is used to find the spacing value
print(value)
print("apcing used :- ",step)

print("# making an array with random values\n")

r = np.random.rand(2,3)
print(r)   


