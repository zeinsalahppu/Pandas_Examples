"""
Pandas Examples
Course: Algorithms and Progeamming for Intelligent sysytems
Semester: SS 2020
"""

import pandas as pd

soccer_df = pd.read_csv("data/england-premier-league-players-2018-to-2019-stats.csv")
print(soccer_df)


# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', 6)
# pd.set_option('display.width', None)
# #pd.set_option('display.max_colwidth', -1)

#print(soccer_df)

compact_soccer = soccer_df[["full_name", "age", "nationality", "Current Club", "position"]]
print(compact_soccer)
# compact_soccer = compact_soccer.set_index('full_name')

# ms = compact_soccer.loc["Mohamed Salah"]
# print(ms)
#
# liverpool_df = compact_soccer.loc[compact_soccer["Current Club"] == "Liverpool"]
# print(liverpool_df)
#
# soccer_over37 = compact_soccer.loc[compact_soccer["age"] > 37]
# print(soccer_over37)

df2 = compact_soccer[["full_name", "age", "nationality"]][compact_soccer["nationality"] == "Spain"]
print(df2)

# p1 = compact_soccer.iloc[0]
# print(p1)
#
# smaller_soccer1_df = compact_soccer.iloc[0:40:5]
# print(smaller_soccer1_df)
#
# smaller_soccer2_df = compact_soccer.iloc[0:40:5, :3]
# print(smaller_soccer2_df)