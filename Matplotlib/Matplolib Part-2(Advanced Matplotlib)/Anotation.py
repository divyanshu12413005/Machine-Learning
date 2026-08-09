import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from DataM import batter

random_batter=batter.head(100).sample(25,random_state=5)

plt.scatter(random_batter['avg'],random_batter['strike_rate'])
plt.xlabel('Average Runs')
plt.ylabel('Strike Rate')
plt.title('Scatter Plot of Batsman Performance')


# giving annotation to each point in the scatter plot

for i in range(random_batter.shape[0]):
    plt.annotate(
        random_batter['batter'].iloc[i],
        (
            random_batter['avg'].iloc[i],
            random_batter['strike_rate'].iloc[i]
        ),
        xytext=(5,5),
        textcoords='offset points',
        fontsize=8
    )
    
    
    # horizonatal and vertical lines to the scatter plot
    plt.axhline(130, color='gray', linestyle='--')
    plt.axvline(30, color='red', linewidth=0.5)
    
plt.show()

