# Numpy : Numerical Python.
# Provides multiple methods and functions to deal with arrays.

import numpy as np
arr1 = np.array([10, 20, 30, 40])   # Creates a numpy array
print(arr1 + 5) # [15 25 35 45]

arr2 = np.arange(0, 10)  # Creates range from 0 to 9
print(arr2)

# Calc Mean, sum, max, min from array.
print(arr1.mean(), arr1.sum(), arr1.max(), arr1.min())  

arr = np.array([1,7,4,3,6,2]) 
print(arr[arr > 3]) # cannot be done using normal array.






# Many of the above things can be done using plain python but numpy is used because :
# Speed : NumPy is implemented in C
# Python doesent provide (arr1 + 5) or arr[arr > 3] and many more operations.