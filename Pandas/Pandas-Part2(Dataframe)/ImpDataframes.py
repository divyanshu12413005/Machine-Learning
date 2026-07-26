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

# batsman_runs['batting_rank'] = batsman_runs['batsman_run'].rank(ascending=False)
# print(batsman_runs.sort_values(by='batting_rank').head(10))

# set_index
batsman_runs.set_index("batter", inplace=True)

# print(batsman_runs)

# reset_index
batsman_runs.reset_index(inplace=True)

# how to replace existing index without losing it

batsman_runs["batting_rank"] = range(1, len(batsman_runs) + 1)

batsman_runs = batsman_runs.set_index("batting_rank")


# print(batsman_runs)

# rename
batsman_runs.rename(columns={"batsman_run": "total_runs"}, inplace=True)    
# print(batsman_runs.head(10))




# Find the last match played by Virat Kohli in Delhi


from ast import literal_eval

# Team players string ko list me convert karo
matches["Team1Players"] = matches["Team1Players"].apply(literal_eval)
matches["Team2Players"] = matches["Team2Players"].apply(literal_eval)

# Dono teams ke players ko merge karo
matches["all_players"] = matches["Team1Players"] + matches["Team2Players"]

# Function
def did_kohli_play(players_list):
    return "V Kohli" in players_list

# New column
matches["did_kohli_play"] = matches["all_players"].apply(did_kohli_play)

# Delhi me Virat ne jo matches khele
kohli_delhi = matches[
    (matches["City"] == "Delhi") &
    (matches["did_kohli_play"] == True)
]

# Latest match
last_match = kohli_delhi.sort_values("Date", ascending=False).head(1)

# print(last_match)


