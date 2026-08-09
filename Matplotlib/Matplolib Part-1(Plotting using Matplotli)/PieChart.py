import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from DataM import gayle


# simple pie chart

# data = [30, 20, 15, 10, 25]
# categories = ['A', 'B', 'C', 'D', 'E']
# plt.pie(data, labels=categories, autopct='%1.1f%%', startangle=90)
# plt.title("Simple Pie Chart")
# plt.show()


# on dataframe

explode = [0,0,0,0.2,0.2,0.2]

plt.figure(figsize=(8,8))

plt.pie(
    gayle['batsman_runs'],
    labels=gayle['batsman'],
    autopct='%1.1f%%',
    explode=explode,
    startangle=90,
    # shadow=True
)

# plt.show()