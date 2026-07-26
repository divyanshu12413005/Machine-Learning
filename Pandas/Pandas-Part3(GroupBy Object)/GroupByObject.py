import numpy as np
import pandas as pd

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import imdb,deliveries


# groupby
genres=imdb.groupby('Genre')

# applying bulitin aggregation functions on groupby object
# print(genres.sum())


# find the top 3 genres by total revenue
top_genres = (
    genres["Gross"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

# print(top_genres)

# find the genre with highest avg imdb rating

highest_avg_rating = (
    genres["IMDB_Rating"]
    .mean()
    .sort_values(ascending=False)
    .head(1)
)
# print(highest_avg_rating)


# find director with most popular
directors = imdb.groupby('Director')

most_popular_director = (
    directors["No_of_Votes"]
    .sum()
    .sort_values(ascending=False)
    .head(1)
)
# print(most_popular_director)    


    # find the heighest rated movie in each genre
    
    
highest_rated_movies = (
    genres.apply(lambda x: x.loc[x['IMDB_Rating'].idxmax()])
    .sort_values(by='IMDB_Rating', ascending=False)
)
# print(highest_rated_movies)



# find number of movies done by each actor

actors = imdb.groupby('Star1')

num_movies_by_actor = actors.size().sort_values(ascending=False).head(10)
# print(num_movies_by_actor)


# agg method  by passing dic

agg_dict = genres.agg(
    {
        "Runtime": "mean",
        "Gross": "sum",
        "IMDB_Rating": "mean",
        "No_of_Votes": "sum",
        "Metascore": "min"
    }
)
# print(agg_dict)


# by passing list

agg_list = genres[
    ["Runtime", "IMDB_Rating", "No_of_Votes", "Gross", "Metascore"]
].agg(["mean", "max", "min"])

# print(agg_list)


# looping on groups

# for genre, group in genres:
#     print("Genre =", genre)
#     print(group)



# split (apply) combine
# apply -> builtin function
# print(genres.min())

# find number of movies starting with A for each group
def foo(group):
    return group["Series_Title"].str.startswith("A").sum()

# print(genres.apply(foo))


# find ranking of each movie in the group based on IMDB rating

def rank_movies(group):
    group["Rank"] = group["IMDB_Rating"].rank(ascending=False)
    return group
# print(genres.apply(rank_movies))


# find the normalized IMDB rating for each movie in the group

def normalize_rating(group):
    group["Normalized_Rating"] = (group["IMDB_Rating"] - group["IMDB_Rating"].min()) / (group["IMDB_Rating"].max() - group["IMDB_Rating"].min())
    return group
# print(genres.apply(normalize_rating))



# group by on  multiple columns

duo=imdb.groupby(['Director','Star1'])

# size

# print(duo.size().sort_values(ascending=False).head(10))

# get_group

# print(duo.get_group(('Christopher Nolan', 'Christian Bale')))

# find the most popular director-actor pair based on most earnings

popular_director_actor_pair = (
    duo["Gross"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
# print(popular_director_actor_pair)

# find the best (in terms of metascore) actor-genre pair

best_actor_genre_pair = (
    imdb.groupby(['Star1', 'Genre'])["Metascore"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
# print(best_actor_genre_pair)

# agg on multiple groupby

# print(
#     duo[["Metascore", "IMDB_Rating"]]
#     .agg(["mean", "sum"])
# )


# print(deliveries.shape)

# find the top 10 batmans in terms of runs

most_runs_batsmen = ( deliveries.groupby("batsman")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
    .head(10))

# print(most_runs_batsmen)

# find the top 10 batmans in terms of most sixes

most_sixes_batsmen = ( deliveries.groupby("batsman")["batsman_runs"]
    .apply(lambda x: (x==6).sum())
    .sort_values(ascending=False)
    .head(10)
)
# print(most_sixes_batsmen) 


# find the batsman with most number of 4s and 6s in last 5 overs of the match

last_5_overs = deliveries[deliveries["over"] > 15]
most_fours_sixes_batsman = ( last_5_overs.groupby("batsman")["batsman_runs"]
    .apply(lambda x: ((x==4) | (x==6)).sum())
    .sort_values(ascending=False)
    .head(10)
)
# print(most_fours_sixes_batsman)


# find V kohli's records against all teams in terms of runs

v_kohli_records = deliveries[deliveries["batsman"] == "V Kohli"]

v_kohli_runs = v_kohli_records.groupby("bowling_team")["batsman_runs"].sum().reset_index()

# print(v_kohli_runs)


# create a function that can return the highest run score of any batsman
def get_highest_run_score(batsman):
    batsman_records = deliveries[deliveries["batsman"] == batsman]
    return batsman_records.groupby('match_id')["batsman_runs"].sum().sort_values(ascending=False).head(1).values[0]

print(get_highest_run_score("MS Dhoni"))
