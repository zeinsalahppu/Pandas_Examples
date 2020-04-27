"""
Pandas Examples
Course: Algorithms and Progeamming for Intelligent sysytems
Semester: SS 2020
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


ice_df = pd.read_csv("data/ics_vs_temp.csv")

temp_list = ice_df["AvgTemperature"]
ice_sales_list = ice_df["IcecreamSales"]

slope, intercept, r, p, std_err = stats.linregress(temp_list, ice_sales_list) # x, y

def line_funtion(x):
  return slope * x + intercept

test_data = np.array([30, 40])
print(line_funtion(test_data))

print(r)

y = line_funtion(temp_list)
plt.scatter(temp_list, ice_sales_list)
plt.plot(temp_list, y)

plt.show()



