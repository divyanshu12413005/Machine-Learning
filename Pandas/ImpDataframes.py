import numpy as np
import pandas as pd

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import matches, movies, batsman_runs, diabetes



# astype

matches["ID"] = matches["ID"].astype("int32")

# print(matches.info())

# value_counts


# print(matches["WinningTeam"].value_counts())
# print(movies["genres"].value_counts())


# find which player has won most potm awards  in final and qualifiers
# print(
#     matches[~matches["MatchNumber"].str.isdigit()]["Player_of_Match"].value_counts()
#     )


# toss dicision team plot

# import matplotlib.pyplot as plt

# matches["TossDecision"].value_counts().plot(kind="bar", title="Toss Decision")

# plt.show()


# how many matches each team has played

# print(
#     (matches["Team1"].value_counts() + matches["Team2"].value_counts())
#     .sort_values(ascending=False)
# )

# rank

batsman_runs['batting_rank'] = batsman_runs['batsman_run'].rank(ascending=False)
print(batsman_runs.sort_values(by='batting_rank').head(10))