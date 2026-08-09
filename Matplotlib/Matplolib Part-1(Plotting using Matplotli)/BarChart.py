import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from DataM import batsmanRecord

# simple bar chart

children=[5,10,15,20,25]
countries=['India','USA','UK','Canada','Australia']

# plt.bar(countries, children)
# plt.xlabel('Countries')
# plt.ylabel('Number of Children')
# plt.title('Population of Different Countries')
# plt.show()

# Horizontal bar chart
# plt.barh(countries, children)
# plt.show()


# multiple bar chart
# Batsman ko index bana do
batsmanRecord.set_index("batsman", inplace=True)

# Multiple bar graph
# batsmanRecord.plot(kind="bar", figsize=(8,5), width=0.8)

# plt.title("Runs Scored by Batsmen")
# plt.xlabel("Batsman")
# plt.ylabel("Runs")
# plt.xticks(rotation=0)   # names seedhe rahenge
# plt.legend(title="Season")
# plt.grid(axis='y', linestyle='--', alpha=0.5)

# plt.show()


# Stacked bar chart

batsmanRecord.plot(kind="bar", stacked=True, figsize=(8,5), width=0.8)
plt.title("Runs Scored by Batsmen")
plt.xlabel("Batsman")
plt.ylabel("Runs")
plt.xticks(rotation=0)
plt.legend(title="Season")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
