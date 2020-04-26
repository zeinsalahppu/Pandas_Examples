"""
Pandas Examples
Course: Algorithms and Progeamming for Intelligent sysytems
Semester: SS 2020
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

flight_df = pd.read_csv("data/raw-flight-data.csv")
# print(flight_df)

# print(flight_df[["DepDelay", "ArrDelay"]].mean())
#
# gbo1 = flight_df.groupby("Carrier")
# print(type(gbo1))
# print(gbo1.mean())
# print(gbo1[["DepDelay", "ArrDelay"]].mean())
#
# gbo2 = flight_df[["Carrier", "DepDelay", "ArrDelay"]].groupby("Carrier")
# print(gbo2.mean())
# print(gbo2.describe())

gbo3 = flight_df.groupby("OriginAirportID")

print(gbo3[["DepDelay", "ArrDelay"]].sum())

print(gbo3[["DepDelay", "ArrDelay"]].agg(lambda x: x[x>0].sum()))

y = gbo3["DepDelay"].agg(lambda x: x[x>0].sum())
x = y.index

fig, ax = plt.subplots()
ax.bar(x, y, 100)
ax.set_yticks( list(range(0, 2000000, 500000)) )
plt.show()