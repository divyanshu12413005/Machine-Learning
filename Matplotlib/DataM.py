from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).parent


gayle = pd.read_csv(
    BASE_DIR / "DataBaseM" / "gayle-175.csv"
    )

batsman = pd.read_csv(
    BASE_DIR / "DataBaseM" / "sharma-kohli.csv"
    )

batter = pd.read_csv(
    BASE_DIR / "DataBaseM" / "batter.csv"
)

batsmanRecord = pd.read_csv(
    BASE_DIR / "DataBaseM" / "batsman_season_record.csv"
)

viratRuns = pd.read_csv(
    BASE_DIR / "DataBaseM" / "vk.csv"
)

bigArray = np.load(
    BASE_DIR / "DataBaseM" / "big-array.npy"
)

iris= pd.read_csv(
    BASE_DIR / "DataBaseM" / "iris.csv"
)

iplBallByBall = pd.read_csv(
    BASE_DIR / "DataBaseM" / "IPL_Ball_by_Ball_2008_2022.csv"
)