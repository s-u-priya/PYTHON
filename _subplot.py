import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 11)
y = np.array([3, 5, 7, 8, 9, 11, 13, 14, 17, 20])
plt.figure(figsize=(8, 9))
# Line Plot
plt.subplot(3, 1, 1)
plt.plot(x, y)
plt.title("Line Plot")
# Scatter Plot
plt.subplot(3, 1, 2)
plt.scatter(x, y)
plt.title("Scatter Plot")
# Bar Plot
plt.subplot(3, 1, 3)
plt.bar(x, y)
plt.title("Bar Plot")
plt.tight_layout()
plt.show()
