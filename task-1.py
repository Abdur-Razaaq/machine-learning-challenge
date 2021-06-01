# importing the python module numpy as np
import numpy as np

#  Used np.arange function to generate 20 numbers starting from 0
x = np.arange(20)

# printing Original Array
print("\nOriginal array:")
print(x)

# Finding Mean
r1 = np.mean(x)
r2 = np.average(x)
assert np.allclose(r1, r2)
# printing mean
print("\nMean: ", r1)

# Standard Deviation
r1 = np.std(x)
r2 = np.sqrt(np.mean((x - np.mean(x)) ** 2))
assert np.allclose(r1, r2)
# printing standard Deviation
print("\nStandard Deviation: ", r2)

# Calculating Variance
r1 = np.var(x)
r2 = np.mean((x - np.mean(x)) ** 2)
assert np.allclose(r1, r2)
# printing Variance
print("\nVariance: ", r1)
