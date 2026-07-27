import numpy as np
import pandas as pd

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import titanic


# creating a timestamp object

# print(
#    type(pd.Timestamp("2026-07-27"))
# )

# giving time also

# print(
#     pd.Timestamp("2026-07-27 12:30:45")
# )

# AM/PM format

# print(
#     pd.Timestamp("2026-07-27 12:30:45 PM")
# )

# print(
#     pd.Timestamp("2026-07-27 12:30:45 AM") 
# )


# using datetime.datetime object

import datetime as dt
# print(
#     pd.Timestamp(dt.datetime(2026, 7, 27, 12, 30, 45))
# )


# fetching attributes 

x=pd.Timestamp("2026-07-27 12:30:45")

# print(x.year)
# print(x.month)
# print(x.day)