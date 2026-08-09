import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from DataM import viratRuns,bigArray


# simple histogram

# data=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
# plt.hist(data, bins=5, edgecolor='black')
# plt.title("Histogram of Data")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()


# on dataframe

# plt.hist(viratRuns['batsman_runs'], bins=10, edgecolor='black')
# plt.title("Histogram of Virat's Runs")
# plt.xlabel("Runs")
# plt.ylabel("Frequency")
# plt.show()


# handling bins
# logarithmic scale
plt.hist(bigArray, bins='auto', edgecolor='black', log=True)
plt.show()