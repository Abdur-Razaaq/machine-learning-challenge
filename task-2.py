# importing numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
# entering arrays and naming them nums and bin respectively
nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])

# printing nums, bin and results where result is data from a histogram
print("nums: ", nums)
print("bins: ", bins)
print("Result:", np.histogram(nums, bins))

# Giving titles and axis names
plt.title("Histogram of nums against bins.")
plt.xlabel("nums")
plt.ylabel("bins")

# plotting histogram with num as x axis and bins as y axis
plt.hist(nums, bins=bins)
# creating graph using gui
plt.show()
