import pandas as pd
import matplotlib.pyplot as plt
# Creating date range
dates = pd.date_range(start="2023-01-01", periods=10, freq='D')
values = [10, 12, 15, 14, 18, 20, 22, 21, 24, 26]
plt.plot(dates, values)
plt.title("Time Series Data")
plt.xlabel("Date")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.show()
