import numpy as np
import pandas as pd

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import matches, movies


# sum -> axis argument

# print(matches.sum(axis=0))  # it will give the sum of each column in the dataframe
# print(matches.sum(axis=1))  # it will give the sum of each row in the dataframe