from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent

subs = pd.read_csv(
    BASE_DIR / "Database" / "subs.csv"
).squeeze()

kohli = pd.read_csv(
    BASE_DIR / "Database" / "kohli_ipl.csv",
    index_col="match_no"
).squeeze()

bollywood = pd.read_csv(
    BASE_DIR / "Database" / "bollywood.csv",
    index_col="movie"
).squeeze()


matches = pd.read_csv(
    BASE_DIR / "Database" / "ipl-matches.csv"
)

movies = pd.read_csv(
    BASE_DIR / "Database" / "movies.csv"
)

batsman_runs = pd.read_csv(
    BASE_DIR / "Database" / "batsman_runs_ipl.csv"
)

diabetes = pd.read_csv(
    BASE_DIR / "Database" / "diabetes.csv"
)

deliveries = pd.read_csv(
    BASE_DIR / "Database" / "deliveries.csv"
    )


imdb = pd.read_csv(
    BASE_DIR / "Database" / "imdb-top-1000.csv"
    )