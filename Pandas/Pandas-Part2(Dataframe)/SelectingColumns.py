import numpy as np
import pandas as pd

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import matches, movies


# single colns

# print(movies['title_x'])  # it will give the series of city column

# multiple colns
# print(movies[['title_x', 'imdb_id']])  # it will give the dataframe of city and country colns



