import numpy as np
import pandas as pd
import seaborn as sn


import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import expense




df=sn.load_dataset('tips')
# print(df.head())

# avg bill paid by male and female

# print(df.pivot_table(index='sex',values='total_bill',aggfunc='mean'))

# avg bill paid by smoker and non-smoker for both male and female
# print(df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='mean',margins=True))


# plotting graph

import matplotlib.pyplot as plt

expense["Date"] = pd.to_datetime(expense["Date"])

expense["month"] = expense["Date"].dt.month_name()

expense.pivot_table(
    index="month",
    columns="Category",
    values="INR",
    aggfunc="sum",
    fill_value=0
).plot(figsize=(10,5))

plt.show()


