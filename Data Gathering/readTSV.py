import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent

df = pd.read_csv(BASE_DIR / "readdatagpt.tsv", sep="\t")

print(df.head())