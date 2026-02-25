import matplotlib.pyplot as plt
import numpy as np
# Sample Data
x = np.arange(1, 11)
y = np.array([2, 4, 5, 6, 8, 10, 12, 14, 15, 18])
# Line Plot
plt.figure()
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
# Bar Plot
plt.figure()
plt.bar(x, y)
plt.title("Bar Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-values")
plt.show()
# Scatter Plot
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-values")
plt.show()
# Histogram
plt.figure()
plt.hist(y)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
