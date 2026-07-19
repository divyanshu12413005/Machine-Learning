import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

subs = pd.read_csv(BASE_DIR.parent / "Database" / "subs.csv").squeeze()

kohli = (
    pd.read_csv(BASE_DIR.parent / "Database" / "kohli_ipl.csv",
                index_col="match_no")
    .squeeze()
)

bollywood = (
    pd.read_csv(BASE_DIR.parent / "Database" / "bollywood.csv",
                index_col="movie")
    .squeeze()
)