# array operations
import numpy as np

print("\n")
print("Array operations")
print("\n")

a = np.array([1,2,3,4,5])
b = np.array([1,1,1,1,1])


print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**2)

print("\n")
print("numpy universal functions")
print("\n")

a = 6

print(np.sqrt(a))
print(np.exp(a))
print(np.log(a))
print(np.sin(a))
print(np.cos(a))

print(np.add.reduce(a)) # this adds all the elements and give a single resulted answer 
print(np.add.accumulate(a)) # this adds elements with previous elements and creates a series

print("\n")
print("Broadcasting")
print("\n")

a = np.array([1,2,3],
             [4,5,6])
b = np.array([10,20,30])

print(a+b) # it adds the elements row by row 

print("Usefull numpy functions")

arr = np.array([1,2,3,4,5,6])

print(np.sum(arr))
print(np.sum(arr,axis=0)) # here axis 0 means column wise sum and 1 means row wise sum
print(np.mean(arr)) # average
print(np.median(arr)) # middle value
print(np.std(arr)) # standard deviation
print(np.var(arr)) # variance
print(np.min(arr)) 
print(np.max(arr))
print(np.argmin(arr)) # index of min value
print(np.argmax(arr)) # index of max value

