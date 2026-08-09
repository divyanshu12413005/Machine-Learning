import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from DataM import iplBallByBall


# on a series

# s=pd.Series(np.random.randn(1000))
# plt.figure(figsize=(8,6))
# s.plot(kind='hist',bins=30,color='blue',alpha=0.5)
# plt.show()


tips=sns.load_dataset('tips')
# print(tips.head())

# scatter plot -> lables -> markers -> color ->cmap

tips.plot(
    kind='scatter',
    x='total_bill',
    y='tip',
    c='size',
    cmap='viridis'
)

plt.show()