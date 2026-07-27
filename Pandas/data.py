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


movies = pd.read_csv(
    BASE_DIR / "Database" / "movies.csv"
)




matches = pd.read_csv(
    BASE_DIR / "Database" / "ipl-matches.csv"
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


courses = pd.read_csv(
    BASE_DIR / "Database" / "courses.csv"
    )

students = pd.read_csv(
    BASE_DIR / "Database" / "students.csv"
    )

nov=pd.read_csv(
    BASE_DIR / "Database" / "reg-month1.csv"
)


dec=pd.read_csv(
    BASE_DIR / "Database" / "reg-month2.csv"
)

ipl=pd.read_csv(
    BASE_DIR / "Database" / "matches.csv"
)

deaths=pd.read_csv(
    BASE_DIR / "Database" / "time_series_covid19_deaths_global.csv"
)

confirm=pd.read_csv(
    BASE_DIR / "Database" / "time_series_covid19_confirmed_global.csv"
)

expense=pd.read_csv(
    BASE_DIR / "Database" / "expense_data.csv"
)

titanic=pd.read_csv(
    BASE_DIR / "Database" / "titanic.csv"
)