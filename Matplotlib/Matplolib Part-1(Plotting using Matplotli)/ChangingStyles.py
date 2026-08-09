import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from DataM import viratRuns,bigArray

# avilable styles

# print(plt.style.available)

# use it on dataframe

plt.style.use('bmh')
plt.hist(viratRuns['batsman_runs'], bins=10, edgecolor='black')
plt.title("Histogram of Virat's Runs")
plt.xlabel("Runs")
plt.ylabel("Frequency")
# plt.show()


# save fugure

plt.savefig("virat_histogram.png", dpi=300, bbox_inches="tight")
plt.show()
