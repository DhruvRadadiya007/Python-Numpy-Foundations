import numpy as np

print("\n")
print(" Random module ")
print("\n")

np.random.seed(42) # Seed = control the starting point of randomness → same seed = same random sequence.

  
print(np.random.randint(1, 10, 6)) # prduces 6 random integers from range 1 to 9
print(np.random.randn(5)) # prints standard normal distribution near 0 that can be negative and positive
print(np.random.rand(5)) # prints uniform distribution values between 0 to 1

