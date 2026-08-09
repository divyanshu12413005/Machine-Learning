import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from DataM import batter


# plot scatter simple graph

x=np.linspace(-10,10,50)
y=x*3+np.random.randint(0,300,50)

# plt.scatter(x,y)
# plt.show()

# scatter on dataframe
plt.scatter(batter.head(50)['avg'],batter.head(50)['strike_rate'])
plt.xlabel('Average')
plt.ylabel('Strike Rate')
plt.title('Average and Strike Rate of top 50 batters')
plt.show()