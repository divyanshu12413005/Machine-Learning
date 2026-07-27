import numpy as np
import pandas as pd

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import titanic


# from strings

x=pd.DatetimeIndex(["2026-07-27 12:30:45", "2026-07-28 12:30:45", "2026-07-29 12:30:45"])
# print(x[0])

# date range function

# generate daily dates in given range

# print(
#     pd.date_range("2026-07-27", "2026-08-05")
# )


# generate dates with given range in alternate days 

# print(
#     pd.date_range("2026-07-27", "2026-08-05", freq="2D")
# )

# B -> Business day frequency

# print(
#     pd.date_range("2026-07-27", "2026-08-05", freq="B")
# )

# W -> Weekly frequency

# print(
#     pd.date_range("2026-07-27", "2026-08-15", freq="W")
# )


# h -> Hourly frequency
print(
    pd.date_range("2026-07-27", "2026-07-28", freq="h")
)

# M -> Month end frequency
# MS -> Month start frequency
# A -> Year end frequency

# using periods(number of results)
print(
    pd.date_range("2026-07-27", periods=10, freq="h")
)