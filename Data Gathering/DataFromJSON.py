import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent

df = pd.read_json(BASE_DIR / "airports.json")

print(df.head())