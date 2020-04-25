"""
Pandas Examples
Course: Algorithms and Progeamming for Intelligent sysytems
Semester: SS 2020
"""

import pandas as pd

# passengers = pd.DataFrame(
#     {
#     "Id": [111, 222, 333, 444, 555],
#     "Name": ["Adam", "Bernhard", "Christina", "Dirk", "Elizabeth"],
#     "Age": [18, 30, 25, 55, 39],
#     "Gender": ["male", "male", "female", "male", "female"]
#     }
# )
#
# print(passengers)

psg_dict = {
    "Id": [111, 222, 333, 444, 555],
    "Name": ["Adam", "Bernhard", "Christina", "Dirk", "Elizabeth"],
    "Age": [18, 30, 25, 55, 39],
    "Gender": ["male", "male", "female", "male", "female"]
    }

passengers_df = pd.DataFrame(psg_dict, columns=["Id", "Name", "Gender", "Age"])

passengers_df.to_excel('passengers.xlsx')



# print(passengers_df.loc[3])
#
# print(passengers_df.loc[[3 , 4]])
#
# print(passengers_df.loc[3, "Age"])
#
# print(passengers_df.loc[passengers_df["Age"] > 27])


# # print(type(passengers_df))
#
# names = passengers_df["Name"]
# print(names)
# # print(type(names))
#
# ages = passengers_df["Age"]
# print(ages)
# print(ages.max())
# print(ages.mean())

