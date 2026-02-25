import numpy as np
# Create a NumPy array
arr = np.array([2, 5, 7, 3, 9, 5, 2, 10, 7])

# Specify a number for comparison
num = 5

# a) Extract numbers less than and greater than a specified number
less_than_num = arr[arr < num]
greater_than_num = arr[arr > num]

print("Array:", arr)
print(f"Numbers less than {num}:", less_than_num)
print(f"Numbers greater than {num}:", greater_than_num)

# b) Find max, min and their indices
print("Maximum value:", np.max(arr))
print("Minimum value:", np.min(arr))
print("Index of Maximum value:", np.argmax(arr))
print("Index of Minimum value:", np.argmin(arr))

# Find unique elements
print("Unique elements:", np.unique(arr))

# Count occurrences of each unique element using bincount
print("Count of each element:", np.bincount(arr))

# Get string representation of the array
print("String representation of array:", repr(arr))



