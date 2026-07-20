import numpy as np
import pandas as pd

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import matches, movies



# find all final winners of IPL matches

# print(
#     matches[matches["MatchNumber"] == "Final"][["Season", "WinningTeam"]]
# )

# how many super over finished have occured

# print(
#     matches[matches["SuperOver"] == "Y"].shape[0]      # here shape[0] gives the number of rows in the filtered dataframe
# )

# how many matches csk have won in kolkata

# print(
#     matches[(matches["WinningTeam"] == "Chennai Super Kings") & (matches["City"] == "Kolkata")].shape[0]
# )


# toss winner is match winner in percentage 
# print(
#     matches[matches["TossWinner"] == matches["WinningTeam"]].shape[0] / matches.shape[0] * 100
# )


# movies with rating greater than 8 and voting greater than 10000

# print(
#     movies[(movies["imdb_rating"] > 8) & (movies["imdb_votes"] > 10000)].shape[0]
# )

# Action movies with rating greater than 7.5

# print(
#     movies[
#         movies["genres"].str.contains("Action", case=False, na=False) &
#         (movies["imdb_rating"] > 7.5)
#     ].shape[0]
# )

# write a function that can return the track records of two teams against each other

team1 = "Mumbai Indians"
team2 = "Chennai Super Kings"

temp = matches[
    matches["Team1"].isin([team1, team2]) &
    matches["Team2"].isin([team1, team2])
]

print("Total Matches :", temp.shape[0])
print()
print(temp["WinningTeam"].value_counts())