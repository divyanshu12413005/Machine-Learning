import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from DataM import batter,viratRuns


fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# 1
axs[0,0].scatter(batter['avg'], batter['strike_rate'])
axs[0,0].set_title("Scatter")
axs[0,0].set_xlabel("Average Runs")
axs[0,0].set_ylabel("Strike Rate")

# 2
axs[0,1].hist(viratRuns['batsman_runs'])
axs[0,1].set_title("Histogram")
axs[0,1].set_xlabel("Batsman Runs")
axs[0,1].set_ylabel("Frequency")

# 3
axs[1,0].bar(batter['runs'], batter['avg'])
axs[1,0].set_title("Bar")
axs[1,0].set_xlabel("Batsman Runs")
axs[1,0].set_ylabel("Average Runs")

# 4
axs[1,1].pie(batter.head(5)['runs'], labels=batter.head(5)['strike_rate'])
axs[1,1].set_title("Pie Chart")
axs[1,1].set_xlabel("Batsman Runs")
axs[1,1].set_ylabel("Strike Rate")

plt.tight_layout()
plt.show()