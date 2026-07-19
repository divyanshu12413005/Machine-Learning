import pandas as pd
import numpy as np  

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import subs, kohli, bollywood


# print(kohli > 50)  # returns boolean series
# print(kohli[kohli >= 50].size)  # returns count of values greater than or equal to 50


# find actors who have done more than 20 movies

actor_count = bollywood.value_counts()

print(actor_count[actor_count > 20])
