"""
Pandas Examples
Course: Algorithms and Progeamming for Intelligent sysytems
Semester: SS 2020
"""

import pandas as pd

flight_df = pd.read_csv("data/raw-flight-data.csv")
print(flight_df)

print(flight_df[["DepDelay", "ArrDelay"]].mean())

gbo1 = flight_df.groupby("Carrier")
print(type(gbo1))
print(gbo1.mean())
print(gbo1[["DepDelay", "ArrDelay"]].mean())

gbo2 = flight_df[["Carrier", "DepDelay", "ArrDelay"]].groupby("Carrier")
print(gbo2.mean())
print(gbo2.describe())

