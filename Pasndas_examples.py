"""
Pandas Examples
Course: Algorithms and Progeamming for Intelligent sysytems
Semester: SS 2020
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

ice_df = pd.read_csv("data/ics_vs_temp.csv")

temp_list = ice_df["AvgTemperature"]
temp_list = temp_list[:, np.newaxis]
ice_sales_list = ice_df["IcecreamSales"]

regr = linear_model.LinearRegression()

regr.fit(temp_list, ice_sales_list)

predicted_ice_sales = regr.predict(temp_list)

test_data = np.array([30, 40])
test_data = test_data[:, np.newaxis]

print(regr.predict(test_data))

plt.scatter(temp_list, ice_sales_list)
plt.plot(temp_list, predicted_ice_sales)
plt.show()
