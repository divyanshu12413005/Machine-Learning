import pandas as pd
import numpy as np  

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import subs, kohli, bollywood


import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from data import subs

# subs.plot()
# plt.show()


bollywood.value_counts().head(20).plot(kind="pie")

plt.show()