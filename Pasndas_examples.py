"""
Pandas Examples
Course: Algorithms and Progeamming for Intelligent sysytems
Semester: SS 2020
"""

import pandas as pd

id_series = pd.Series([111, 222, 333, 444, 555])
name_series = pd.Series(["Adam", "Bernhard", "Christina", "Dirk", "Elizabeth"])
age_series = pd.Series([18, 30, 25, 55, 39])
gender_series = pd.Series(["male", "male", "female", "male", "female"])

# option 1 to define column labels
id_series.name = "Id"
name_series.name = "Name"
age_series.name = "Age"
gender_series.name = "Gender"

psg_df = pd.concat([id_series, name_series, age_series, gender_series], axis=1)
print(psg_df)


# # option 2 to define column labels
# psg_df = pd.concat([id_series, name_series, age_series, gender_series], axis=1)
#
# col_labels = ["Id", "Name", "Age", "Gender"]
# psg_df.columns = col_labels
# print(psg_df)